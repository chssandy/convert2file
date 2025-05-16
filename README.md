## convert2file

**Author:** [chssandy](https://github.com/chssandy)

**Github Repository:** https://github.com/chssandy/convert2file

**Dify Marketplace:** https://marketplace.dify.ai/plugins/chssandy/convert2file

**Version:** 0.0.1

**Type:** tool

### Description
Convert2File is a powerful file conversion tool designed to meet modern document processing needs. It excels at converting multiple language formats such as Markdown, HTML, and others into widely-used document formats like DOCX and PDF, with a particular strength in handling mathematical symbols seamlessly.

Key Features:

Versatile Document Conversion: Whether you need to convert from Markdown to DOCX or from HTML to PDF, Convert2File makes it effortless, ensuring your documents migrate smoothly across different platforms without losing quality.

Exceptional Support for Mathematical Symbols: 
One of the standout features of this software is its robust support for mathematical symbols. Whether you're working on academic papers, technical documents, or educational materials that include complex formulas, Convert2File ensures accurate and flawless conversions, maintaining the professionalism and precision of your original content.
By using Convert2File, you can significantly streamline the process of document sharing and publishing while ensuring all elements—especially intricate mathematical expressions—are rendered with the highest quality.

## Convert2File 软件介绍
Convert2File 是一款功能强大的文件转换工具，专为满足现代文档处理需求而设计。它能够将 Markdown、HTML 等多种文件格式转换为 DOCX、PDF 等常用文档格式，并且特别支持数学符号的完美转换。

主要特色：

多种文档格式之间的转换：无论是从 Markdown 到 DOCX，还是从 HTML 到 PDF，Convert2File 都能轻松应对，确保您的文档在不同平台间无缝迁移。

卓越的数学符号支持：该软件的一大亮点是其对数学符号的支持。无论是在学术论文、技术文档还是教育资料中包含的复杂公式，Convert2File 都能准确无误地进行转换，保留原始文档的专业性和准确性。

通过使用 Convert2File，保证所有内容——包括复杂的数学表达式——都能以最高质量呈现。

## parameters description
| 参数   | 示例    | 说明    |
| ---- | ---- | ---- |
| input_text   | string  | 需要转换的文本   |
| input_filetype   | markdown｜html    |  文本语法  |
| output_filetype     |  docx｜pdf    |   期望生成的文件类型   |
| remove_think_prompt | true｜false | 是否移除思考提示 |


### Usage
![alt text](/_assets/example.png)



### 依赖 important！important！important！
**The PDF export functionality of this project depends on the LaTeX engine. Please make sure that a LaTeX environment is properly installed on the server.**
**本项目导出pdf格式依赖latex引擎，请确保服务器安装了latex环境**
- Mac：mactex
- Linux：texlive
- Window：latex

**提示：请根据实际情况安装对应的latex环境，并确保latex环境正常可用。**
![alt text](/_assets/latex_canuse.png)


## 版本更新

- 0.0.1：初始版本，支持 markdown 转换为 docx 和 pdf


