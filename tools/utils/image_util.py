import os
import requests
import re
from urllib.parse import urlparse


class ImageUtil:
    @staticmethod
    def get_image_size(image_path):
        """
        获取图像的尺寸（宽度和高度）。
        
        参数:
        - image_path: 图像文件的路径。

        返回:
        - 一个元组 (width, height)。
        """
        from PIL import Image
        with Image.open(image_path) as img:
            return img.size

    @staticmethod
    def resize_image(image_path, size):
        """
        调整图像的大小并保存到原路径。

        参数:
        - image_path: 图像文件的路径。
        - size: 目标尺寸，格式为 (width, height)。
        """
        from PIL import Image
        with Image.open(image_path) as img:
            img = img.resize(size)
            img.save(image_path)

    @staticmethod
    def download_image(url, folder):
        """
        下载网络图片并保存到指定目录。

        参数:
        - url: 图像的 URL 地址。
        - folder: 图像保存的目标目录。

        返回:
        - 本地保存的图像路径。
        """
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        filepath = os.path.join(folder, filename)

        if not os.path.exists(filepath):
            response = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        return filepath

    @staticmethod
    def preprocess(text, temp_dir):
        """
        预处理 文本，将网络图片链接替换为本地路径。

        参数:
        - text: 原始 文本。
        - temp_dir: 下载图片的临时存储目录。

        返回:
        - 替换后的 文本，其中的图片链接指向本地路径。
        """
        # 使用正则表达式匹配 Markdown 中的图片语法：![](url)
        img_pattern = re.compile(r'!$.*?$$(.*?)$')
        for match in img_pattern.finditer(text):
            url = match.group(1)
            if url.startswith('http'):
                local_path = ImageUtil.download_image(url, temp_dir)
                text = text.replace(url, local_path)
        return text