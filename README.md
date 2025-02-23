# Manga OCR and Translation Tool

## 项目简介

这是一个用于识别日文漫画中的文本并将其翻译成中文的工具。它结合了 **Manga OCR** 和 **Kimi API**，支持自动截图、OCR 识别和翻译。通过 **ShareX** 截图工具，用户可以方便地捕获屏幕区域，将截图路径复制到剪贴板，然后自动触发 OCR 和翻译功能。

## 项目依赖

本项目基于以下库和项目实现，感谢这些开源项目的贡献：

- **Manga OCR**: 用于日文文本识别。  
  [GitHub - kha-white/manga-ocr](https://github.com/kha-white/manga-ocr)

- **Kimi API**: 用于日文到中文的翻译。  
  [Kimi 开放平台](https://platform.moonshot.cn)

- **Pyperclip**: 用于操作剪贴板。  
  [GitHub - asweigart/pyperclip](https://github.com/asweigart/pyperclip)

- **OpenAI**: 用于调用 Kimi API。  
  [OpenAI Python SDK](https://github.com/openai/openai-python)

- **AutoHotkey**: 用于创建热键触发脚本。  
  [AutoHotkey 官方网站](https://www.autohotkey.com/)

## 项目文件结构

- `run_kimitranslation.bat`: 用于激活虚拟环境并运行 Python 脚本的批处理文件。
- `kimitranslation.py`: Python 脚本，用于监控剪贴板内容，识别图片中的日文并翻译成中文。

## 安装和使用说明

### 安装依赖

1. **安装 Python 3.6 或更高版本**  
   从 [Python 官网](https://www.python.org/) 下载并安装。

2. **安装必要的 Python 库**  
   打开终端执行以下命令：
   ```bash
   pip install pyperclip manga_ocr openai
   ```

3. **安装 AutoHotkey**  
   访问 [AutoHotkey 官方网站](https://www.autohotkey.com/) 下载并安装。

### 运行项目

#### 激活虚拟环境

1. 打开命令提示符，导航到项目目录：
   ```bash
   cd C:\Users\Dell\Documents\manga_ocr-0.1.14
   ```

2. 激活虚拟环境：
   ```bash
   .\venv\Scripts\activate
   ```

#### 运行 Python 脚本

在激活的虚拟环境中运行脚本：
```bash
python kimitranslation.py
```

#### 运行批处理脚本

双击 `run_kimitranslation.bat` 文件，自动激活虚拟环境并运行 Python 脚本。

#### （可按需选择）使用 AutoHotkey 脚本
例如：
1. 将 `ConvertToTraditional.ahk` 文件保存到项目目录。
2. 双击 `ConvertToTraditional.ahk` 文件运行脚本。
3. 选中需要转换的文本，按鼠标侧边键（`XButton1`）触发转换。

### 使用 ShareX 截图

#### 安装 ShareX

访问 [ShareX 官网](https://getsharex.com/) 下载并安装 ShareX。

#### 配置 ShareX

1. 打开 ShareX 设置，选择“截图后”选项。
2. 勾选“保存图像文件”和“将文件路径复制到剪贴板”。
3. 设置截图保存路径，例如：  
   `C:\Users\Dell\Documents\manga_ocr-0.1.14\screenshots`

#### 截图并触发 OCR 和翻译

1. 使用 ShareX 截图工具捕获屏幕区域，截图路径将自动复制到剪贴板。
2. Python 脚本会自动检测剪贴板中的图像路径并触发 OCR 和翻译功能。

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库。
2. 创建新的特性分支：
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 提交更改：
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. 推送到分支：
   ```bash
   git push origin feature/AmazingFeature
   ```
5. 创建 Pull Request。

## 开源协议

本项目采用 **MIT License**。详情请参阅 [LICENSE 文件](https://github.com/your-username/your-repo/blob/main/LICENSE)。



