'use strict';
// Static file server for the Copilot Multi-Industry Demo Hub on Azure App Service
// (Linux, Node). No dependencies. Serves ./public with directory index pages,
// trailing-slash redirects, gzip for text files, byte ranges for large files, and
// the headers the old Static Web Apps configuration used to set.
const http = require('http');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const ROOT = path.join(__dirname, 'public');
const PORT = Number(process.env.PORT) || 8080;
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.htm': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8', '.md': 'text/markdown; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8', '.xml': 'application/xml; charset=utf-8',
  '.svg': 'image/svg+xml', '.ipynb': 'application/x-ipynb+json',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
  '.webp': 'image/webp', '.ico': 'image/x-icon', '.woff': 'font/woff', '.woff2': 'font/woff2',
  '.pdf': 'application/pdf', '.zip': 'application/zip', '.eml': 'message/rfc822',
  '.mp3': 'audio/mpeg', '.mp4': 'video/mp4',
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
};
const COMPRESSIBLE = new Set(['.html', '.htm', '.js', '.mjs', '.css', '.json', '.txt', '.md', '.csv', '.xml', '.svg', '.ipynb', '.eml']);
const BASE_HEADERS = { 'X-Robots-Tag': 'noindex, nofollow', 'X-Content-Type-Options': 'nosniff' };
const gzCache = new Map();

function notFound(res, head) {
  const body = '<!DOCTYPE html><meta charset="UTF-8"><meta name="robots" content="noindex"><title>Not found</title>' +
    '<p style="font-family:system-ui;margin:40px">This page does not exist. <a href="/">Open the Copilot Multi-Industry Demo Hub</a>.</p>';
  res.writeHead(404, { ...BASE_HEADERS, 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': Buffer.byteLength(body), 'Cache-Control': 'no-cache' });
  res.end(head ? undefined : body);
}

function gzipped(file, st, cb) {
  const hit = gzCache.get(file);
  if (hit && hit.mtimeMs === st.mtimeMs && hit.size === st.size) return cb(null, hit.buf);
  fs.readFile(file, (err, raw) => {
    if (err) return cb(err);
    zlib.gzip(raw, { level: 9 }, (zerr, buf) => {
      if (zerr) return cb(zerr);
      gzCache.set(file, { mtimeMs: st.mtimeMs, size: st.size, buf });
      cb(null, buf);
    });
  });
}

function serveFile(req, res, file, st, urlPath) {
  const ext = path.extname(file).toLowerCase();
  const head = req.method === 'HEAD';
  const etag = `W/"${st.size.toString(16)}-${Math.floor(st.mtimeMs).toString(16)}"`;
  const noCache = ext === '.html' || ext === '.htm' || urlPath === '/data.js';
  const headers = {
    ...BASE_HEADERS,
    'Content-Type': TYPES[ext] || 'application/octet-stream',
    'Cache-Control': noCache ? 'no-cache' : 'public, max-age=3600',
    'Last-Modified': st.mtime.toUTCString(),
    ETag: etag,
    'Accept-Ranges': 'bytes',
  };
  if (COMPRESSIBLE.has(ext)) headers.Vary = 'Accept-Encoding';
  if (req.headers['if-none-match'] === etag) {
    res.writeHead(304, headers);
    return res.end();
  }

  const range = req.headers.range;
  const wantsGzip = /\bgzip\b/.test(req.headers['accept-encoding'] || '');
  if (!range && wantsGzip && COMPRESSIBLE.has(ext) && st.size > 1024) {
    return gzipped(file, st, (err, buf) => {
      if (err) return notFound(res, head);
      res.writeHead(200, { ...headers, 'Content-Encoding': 'gzip', 'Content-Length': buf.length });
      res.end(head ? undefined : buf);
    });
  }

  let start = 0;
  let end = st.size - 1;
  let status = 200;
  if (range) {
    const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
    if (m && (m[1] !== '' || m[2] !== '')) {
      if (m[1] === '') {
        start = Math.max(st.size - Number(m[2]), 0);
      } else {
        start = Number(m[1]);
        if (m[2] !== '') end = Math.min(Number(m[2]), st.size - 1);
      }
    }
    if (!m || start > end || start >= st.size) {
      res.writeHead(416, { ...BASE_HEADERS, 'Content-Range': `bytes */${st.size}` });
      return res.end();
    }
    status = 206;
    headers['Content-Range'] = `bytes ${start}-${end}/${st.size}`;
  }
  headers['Content-Length'] = end - start + 1;
  res.writeHead(status, headers);
  if (head || st.size === 0) return res.end();
  const stream = fs.createReadStream(file, { start, end });
  stream.on('error', () => res.destroy());
  stream.pipe(res);
}

const server = http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, { ...BASE_HEADERS, Allow: 'GET, HEAD' });
    return res.end();
  }
  const head = req.method === 'HEAD';
  let rawPath;
  let query;
  let urlPath;
  try {
    const u = new URL(req.url, 'http://localhost');
    rawPath = u.pathname;
    query = u.search;
    urlPath = decodeURIComponent(rawPath);
  } catch (e) {
    res.writeHead(400, BASE_HEADERS);
    return res.end('Bad request');
  }
  if (urlPath.includes('\0') || urlPath.split(/[\\/]/).some((seg) => seg.startsWith('.') && seg.length > 0)) {
    return notFound(res, head);
  }
  const file = path.join(ROOT, path.normalize(urlPath));
  if (file !== ROOT && !file.startsWith(ROOT + path.sep)) return notFound(res, head);

  fs.stat(file, (err, st) => {
    if (err) return notFound(res, head);
    if (st.isDirectory()) {
      if (!rawPath.endsWith('/')) {
        // Collapse leading slashes so the Location can never become a
        // protocol-relative URL that points at another host.
        const location = '/' + rawPath.replace(/^[/\\]+/, '') + '/' + query;
        res.writeHead(301, { ...BASE_HEADERS, Location: location, 'Cache-Control': 'no-cache' });
        return res.end();
      }
      const index = path.join(file, 'index.html');
      return fs.stat(index, (ierr, ist) => (ierr || !ist.isFile() ? notFound(res, head) : serveFile(req, res, index, ist, urlPath + 'index.html')));
    }
    if (!st.isFile()) return notFound(res, head);
    serveFile(req, res, file, st, urlPath);
  });
});

// Azure front ends keep connections open longer than Node's 5-second default.
server.keepAliveTimeout = 65000;
server.headersTimeout = 66000;
server.listen(PORT, () => {
  console.log(`Copilot Multi-Industry Demo Hub serving ${ROOT} on port ${PORT}`);
  for (const warm of ['data.js', 'hub.html', 'index.html']) {
    const f = path.join(ROOT, warm);
    fs.stat(f, (err, st) => { if (!err) gzipped(f, st, () => {}); });
  }
});
