import logging
import tempfile
import io
from docx import Document
import pypandoc

from tools.utils import file_util

def get_docx_bytes(input_text: str, output_filetype: str, output_extension: str) -> bytes:
    with tempfile.NamedTemporaryFile(suffix=output_extension, delete=True) as tmpfile:
        output = pypandoc.convert_text(
            source=input_text,
            to=output_filetype,
            format="markdown+tex_math_dollars",
            outputfile=tmpfile.name,
            extra_args=["--mathjax","--mathml"],
            # extra_args=["--mimetex"],  # 图片方式输出公式
            # extra_args=["--mathml"],
            encoding="utf-8"
        )
        if output:
            raise RuntimeError(f"Pandoc error: {output}")

        # 重新加载 .docx 文件
        doc = Document(tmpfile.name)

    if file_util.is_contains_chinese_chars(input_text):
        doc = file_util.set_chinese_fonts(doc)

    # 保存到 BytesIO
    result_bytes_io = io.BytesIO()
    doc.save(result_bytes_io)
    result_file_bytes = result_bytes_io.getvalue()
   
    return result_file_bytes
    
