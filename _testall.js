const fs = require('fs');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync('hub.html', 'utf8');
const data = fs.readFileSync('data.js', 'utf8');
const dom = new JSDOM(html, { runScripts: 'outside-only', url: 'http://localhost/' });
const w = dom.window;
Object.defineProperty(w, 'sessionStorage', { value: { getItem:()=>'ok', setItem:()=>{}, removeItem:()=>{} }, writable: true });
// Silence scrollTo
w.scrollTo = ()=>{};
w.eval(data);
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
w.eval(scriptMatch[1]);
let pass=0, fail=0;
for (const item of w.HUB_DATA.industries) {
  try { w.showItem(item, 'ind'); pass++; }
  catch(e){ fail++; console.log('FAIL', item.id, '--', e.message); }
}
console.log('IND:', pass, 'OK,', fail, 'FAIL of', w.HUB_DATA.industries.length);
pass=0; fail=0;
for (const item of w.HUB_DATA.departments) {
  try { w.showItem(item, 'dept'); pass++; }
  catch(e){ fail++; console.log('FAIL DEPT', item.id, '--', e.message); }
}
console.log('DEPT:', pass, 'OK,', fail, 'FAIL of', w.HUB_DATA.departments.length);
