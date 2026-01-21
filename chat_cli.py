# TinySwallow Simple CLI Chat App for Raspberry Pi
# Requires: llama.cpp compiled and model downloaded as "tinyswallow.gguf"
"""
2026/01/14  簡易Chatプログラム

本ソフトウェアは、Ollama Python Client（MIT License）を使用しています。
Copyright (c) Ollama contributors.

Copyright (c) 2026 takanobu Kawabata
All rights reserved.
This software uses the Ollama Python client (MIT License).
Ollama is not affiliated with this product.
"""

import ollama
import subprocess
import readline  # for better CLI input experience

# LLMモデルをダウンロード
subprocess.run(["python", "model_downloader.py"], check=True)
# 使用モデルを指定
model_name = "tinyswallow"

def chat_with_model(prompt):
    stream = ollama.chat(
    model=model_name,
    messages=[{'role': 'user', 'content': prompt}],
    stream=True, # ストリーミングを有効化
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def main():
    print("TinySwallow Chat (Raspberry Pi CLI)")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You:").strip()
        if user_input.lower() in ["exit", "quit","bye","end"]:
            print("Goodbye!")
            break
        print("AI:")
        response = chat_with_model(user_input)
        print()

if __name__ == "__main__":
    main()
