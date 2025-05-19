import tempfile
import pypandoc


def get_pdf_bytes(input_text: str, output_filetype: str, output_extension: str) -> bytes:
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=True) as tmpfile:
        output = pypandoc.convert_text(
            source=input_text,
            to="pdf",
            format="markdown+tex_math_dollars",
            outputfile=tmpfile.name,
            extra_args=[
                "--pdf-engine=xelatex",
                "-V", "mainfont=WenQuanYi Zen Hei",
                "-V", "fontsize=12pt",
                "-V", "documentclass=article",
                "-V", "geometry:margin=1in",
                "-V", "math-style=TeX",
                "-V", r'header-includes='
                    r'\usepackage{amsmath}'
                    r'\usepackage{amssymb}'
                    r'\usepackage{microtype}'
                    r'\usepackage{xurl}'
                    r'\usepackage[AutoFakeBold=true, AutoFakeSlant=true]{xeCJK}',
                "-V", "CJKglue=\\hskip 0.15em plus 0.05em minus 0.05em",  # 调整 CJK 字符之间的间距
                "-V", "xeCJK-space=true"  # 启用 xeCJK 空格支持
            ],
            encoding="utf-8"
        )
        if output:
            raise RuntimeError(f"Pandoc error: {output}")

        # 直接读取 PDF 文件内容为 bytes
        with open(tmpfile.name, "rb") as f:
            result_file_bytes = f.read()

   
    return result_file_bytes
    