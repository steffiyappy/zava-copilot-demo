"""Top-level orchestrator that runs all regulator+cross-dept stub builders."""
from gen_reg_pdfs import BUILDERS as PDF_BUILDERS
from gen_reg_docxs import BUILDERS as DOCX_BUILDERS
from gen_reg_xlsxs_a import BUILDERS as XLSX_A
from gen_reg_xlsxs_b import BUILDERS as XLSX_B

ALL = PDF_BUILDERS + DOCX_BUILDERS + XLSX_A + XLSX_B


def main():
    print(f"Running {len(ALL)} regulator stub builders...")
    for fn in ALL:
        fn()
        print(" - wrote", fn.__name__)
    print(f"\nDone. {len(ALL)} files generated.")


if __name__ == "__main__":
    main()
