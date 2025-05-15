# -*- coding: utf-8 -*-
# -*- author: CHS -*-

import re
from docx.oxml.ns import qn


def strip_wrapper(text: str, input_type: str) -> str:
    """
    移除文本两端的空白字符以及可能存在的代码块包裹符号（如 ```markdown ... ```）。

    参数:
    - text: 输入的文本字符串。
    - mime_type: 动态传入的 MIME 类型，用于识别代码块类型（如 markdown）。

    返回:
    - 去除包裹符号和空格后的文本。
    """
    # 去除首尾空白字符
    text = text.strip()
    wrapper = "```"
    # 如果文本以代码块结束符结尾，则尝试去除包裹符号
    if text.endswith(wrapper):
        if text.startswith(wrapper):
            # 完全匹配包裹符，直接去除前后包裹符
            text = text[len(wrapper): -len(wrapper)]
        elif text.startswith(f"{wrapper}{input_type}"):
            # 带 MIME 类型的包裹符，去除前缀和后缀
            text = text[(len(f"{wrapper}{input_type}")): -len(wrapper)]
    return text


def is_contains_chinese_chars(text: str) -> bool:
    """
    判断给定文本中是否包含中文字符。

    参数:
    - text: 需要检测的文本字符串。

    返回:
    - True 如果包含中文字符，否则 False。
    """
    return bool(re.search(r'[\u4e00-\u9fff]', text))


def set_chinese_fonts(doc):
    """
    为生成的 Word 文档设置中文字体样式。
    参数:
    - doc: python-docx 文档对象。
    """
    # 获取 Normal 样式并设置字体
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'  # 设置西文字体

    rPr = style.element.get_or_add_rPr()
    rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 设置中文字体为宋体
    return doc