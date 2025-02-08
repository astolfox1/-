import pyperclip
import time
import os
from manga_ocr import MangaOcr
from openai import OpenAI

# 初始化 Manga OCR
mocr = MangaOcr()

# 初始化 Kimi API 客户端
client = OpenAI(
    api_key="sk-eTAJnHE0m3yXprkuKkvKEVmkusQ4PJIVrRlfJZFgoKkWKpQV",  # 替换为你的 Kimi API Key
    base_url="https://api.moonshot.cn/v1",
)

def recognize_and_translate(image_path):
    try:
        # 识别图像中的文本
        text = mocr(image_path)
        print(f"OCR Result: {text}")

        # 调用 Kimi API 进行翻译
        completion = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system", "content": "将以下日文文本翻译成中文"},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
        )

        # 获取翻译结果
        translated_text = completion.choices[0].message.content
        print(f"Translated Text: {translated_text}")

        # 将原文和翻译结果保存到剪贴板
        clipboard_content = f"{text}\n{translated_text}"
        pyperclip.copy(clipboard_content)
        print("Content copied to clipboard.")
    except Exception as e:
        print(f"Error processing image: {e}")

def monitor_clipboard():
    last_clipboard_content = ""
    while True:
        # 获取当前剪贴板内容
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != last_clipboard_content:
            last_clipboard_content = current_clipboard_content
            print(f"Detected new clipboard content: {current_clipboard_content}")

            # 检查剪贴板内容是否为有效的图像路径
            if os.path.isfile(current_clipboard_content):
                print(f"Detected new image in clipboard: {current_clipboard_content}")
                recognize_and_translate(current_clipboard_content)
            else:
                print("Clipboard content is not a valid image path.")
        time.sleep(1)

if __name__ == "__main__":
    print("Monitoring clipboard for images...")
    monitor_clipboard()