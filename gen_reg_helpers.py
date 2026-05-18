"""Shared helpers for regulator stub-file generators.

Reuses _xlsx/_docx/_pdf from gen_cowork_files.py without triggering its
top-level build (which would generate the original Cowork sample files).
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES_DIR = ROOT / "files"
FILES_DIR.mkdir(exist_ok=True)


def _load_gen():
    spec = importlib.util.spec_from_file_location(
        "_g", str(ROOT / "gen_cowork_files.py")
    )
    mod = importlib.util.module_from_spec(spec)
    prev = sys.argv
    sys.argv = ["_g"]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = prev
    return mod


_g = _load_gen()
_docx = _g._docx
_pdf = _g._pdf
_xlsx = _g._xlsx


def out(name: str) -> str:
    return str(FILES_DIR / name)


__all__ = ["_docx", "_pdf", "_xlsx", "out", "FILES_DIR"]
