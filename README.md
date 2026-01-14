# LLM_chat
LLMによるチャットシステム<br>

<h4><<概要>></h4>
LLMフレームワークであるollamaを使って、TinySwallowをモデルにしたチャットシステムです。<br>
CLIシステムとWebシステムがあります。

<h4><<システム構成>></h4>
/home/pi/LLM_chat/
│
├── model_downloader.py      ← モデルDL用スクリプト
│
├── chat_cli.py              ← CLIチャット用Python
│
├── app.py                   ← Webチャット用Python
├── templates/
│   └── index.html           ←  Webチャット用html
│
├── start.sh                 ← 起動用ワンクリック
├── 利用規約.txt 
├── License.txt 
└── README.txt               ← 紙マニュアル代わり


