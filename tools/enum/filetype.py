from enum import StrEnum

class SyntaxFormat(StrEnum):
    MARKDOWN = "markdown"
    PYTHON = "python"
    HTML = "html"
    ECHART = "echart"

class FileType(StrEnum):
    CSS = "css"
    CSV = "csv"
    DOCX = "docx"
    HTML = "html"
    JS = "js"
    JAVA = "java"
    JSON = "json"
    LATEX = "latex"
    MD = "md"
    PDF = "pdf"
    PHP = "php"
    PNG = "png"
    PPTX = "pptx"
    PY = "py"
    RST = "rst"
    RUBY = "ruby"
    SH = "sh"
    TXT = "txt"
    XLSX = "xlsx"
    YAML = "yaml"
    XML = "xml"
    ZIP = "zip"

    @classmethod
    def get_mime(cls, mime_type: str) -> str:
        mime_type_map = {
            cls.CSS: "text/css",
            cls.CSV: "text/csv",
            cls.DOCX: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            cls.HTML: "text/html",
            cls.JS: "text/javascript",
            cls.JAVA: "text/x-java-source",
            cls.JSON: "application/json",
            cls.LATEX: "application/x-tex",
            cls.MD: "text/markdown",
            cls.PDF: "application/pdf",
            cls.PHP: "application/x-httpd-php",
            cls.PNG: "image/png",
            cls.PPTX: "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            cls.PY: "text/x-python",
            cls.RST: "text/prs.fallenstein.rst",
            cls.RUBY: "text/x-ruby",
            cls.TXT: "text/plain",
            cls.SH: "application/x-sh",
            cls.XLSX: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            cls.XML: "text/xml",
            cls.YAML: "text/yaml",
            cls.ZIP: "application/zip",
        }
        return mime_type_map.get(mime_type, ".bin")