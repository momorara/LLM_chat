import ollama
import subprocess
from flask import Flask, render_template, request, Response

MODEL_NAME = "tinyswallow"

# 初回モデルDL（あれば何もしない）
subprocess.run(["python3", "model_downloader.py"], check=False)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# ===== ストリーミングAPI =====
@app.route("/chat_stream")
def chat_stream():
    user_message = request.args.get("message", "")

    def generate():
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": user_message}],
            stream=True
        )

        for chunk in stream:
            text = chunk["message"]["content"]
            # SSE形式で送信
            yield f"data: {text}\n\n"

    return Response(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
