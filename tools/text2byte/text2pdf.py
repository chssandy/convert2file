import logging
import tempfile
import io
from docx import Document
import markdown
import pypandoc
from xhtml2pdf import pisa

from tools.utils import file_util

def get_pdf_bytes(input_text: str, output_filetype: str, output_extension: str) -> bytes:
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=True) as tmpfile:
        print(input_text)
        output = pypandoc.convert_text(
            source=input_text,
            to="pdf",
            format="markdown+tex_math_dollars",
            outputfile=tmpfile.name,
            extra_args=[
                "--pdf-engine=xelatex",
                "-V", "mainfont=Songti SC",
                "-V", "fontsize=12pt",
                "-V", "geometry:margin=1in",
                "-V", "documentclass=article",
                "-V", "math-style=TeX"
            ],
            encoding="utf-8"
        )
        if output:
            raise RuntimeError(f"Pandoc error: {output}")

        # 直接读取 PDF 文件内容为 bytes
        with open(tmpfile.name, "rb") as f:
            result_file_bytes = f.read()

   
    return result_file_bytes
    