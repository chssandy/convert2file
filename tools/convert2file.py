import io
import logging
import tempfile
from typing import Generator
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from docx import Document
import pypandoc
import uuid


from tools.enum import filetype
from tools.text2byte.text2pdf import get_pdf_bytes
from tools.utils import file_util
from tools.utils.image_util import ImageUtil
from tools.utils.param_util import get_input_text, get_input_filetype, get_output_filetype
from tools.text2byte.text2word import get_docx_bytes


class Md2DocxTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        invoke tools
        """
        # get parameters
        with tempfile.TemporaryDirectory() as temp_dir:
            input_text = get_input_text(tool_parameters)
            input_text = ImageUtil.preprocess(input_text, temp_dir)
            output_filetype = get_output_filetype(tool_parameters)
            output_extension = f".{output_filetype}"
            output_filename = f"{str(uuid.uuid4()).upper()}{output_extension}"

            try:
                if output_filetype == filetype.FileType.DOCX:
                    result_file_bytes = get_docx_bytes(input_text, output_filetype, output_extension)
                elif output_filetype == filetype.FileType.PDF:
                    result_file_bytes = get_pdf_bytes(input_text, output_filetype, output_extension)


                    
            except Exception as e:
                logging.exception("Failed to convert file")
                yield self.create_text_message(f"Failed to convert markdown text to {output_filetype} file, error: {str(e)}")
                return
            logging.debug("准备发送 blob 数据")
            yield self.create_blob_message(
                blob = result_file_bytes,
                meta = {
                    "mime_type": filetype.FileType.get_mime(output_filetype),
                    "filename": output_filename,
                }
            )
            logging.debug("blob 数据发送完成")
            return


    
