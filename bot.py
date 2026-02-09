import json
import threading
from flask import Flask, request
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ========= BOT CREDIT =========
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"

# ========= TOKEN =========
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"

# ========= ADMIN ID =========
ADMIN_ID = 5887665463

# ========= SERVER =========
flask_app = Flask(__name__)

# ========= START =========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["1️⃣ ترمیکس کمانډونه"],
        ["2️⃣ سالار کمانډ"],
        ["3️⃣ کورنا لیکنې"],
        ["4️⃣ چت روم"],
        ["5️⃣ ترمیکس ډاونلوډ"],
        ["6️⃣ د سالار واتساف"],
        ["7️⃣ د کورنا سوی ایدی جوړول"],
        ["8️⃣ نوی برخه"]
    ]
    await update.message.reply_text(
        f"👋 سلام!\nیو انتخاب وکړئ 👇\n\n{BOT_CREDIT}",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# ========= TERMUX =========
async def termux_commands(update, context):
    await update.message.reply_text("""
📌 Termux Commands:

pkg update
pkg upgrade
pkg install python
pkg install git
pip install requests
pip install mechanize
pip install bs4 futures
pip install rich
termux-setup-storage
pip install pycurl
""")

# ========= SALAR =========
async def salar_command(update, context):
    await update.message.reply_text("""
📌 Salar Command:

rm -rf SALAR
git clone --depth=1 https://github.com/SaLarKhAnOo2003/SALAR.git
cd SALAR
python SALAR.py
""")

# ========= CONDOLENCE =========
async def condolence(update, context):
    await update.message.reply_text("""
🕊️ کورنا لیکنې:

---------------------------------------------------
The news of your death came to my ears like a gun shot😭.
R.I.P bro 💔
---------------------------------------------------
""")

# ========= CHAT =========
async def chat_room(update, context):
    await update.message.reply_text(
        "💬 چت روم:\n\n"
        "سلام زه سالار خانو یم\n"
        "زه کندهاری یم 🇦🇫\n"
        "هر ځای سالار زنداباد ✌️"
    )

# ========= DOWNLOAD =========
async def termux_download(update, context):
    await update.message.reply_text("""
📥 Termux Download:

https://f-droid.org/packages/com.termux/
https://github.com/termux/termux-app/releases
https://apkpure.com/termux/com.termux
https://apkcombo.com/termux/com.termux/
https://uptodown.com/android/termux
""")

# ========= WHATSAPP =========
async def whatsapp(update, context):
    await update.message.reply_text(
        "💬 WhatsApp Group:\n\n"
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

# ========= MEMORIAL =========
async def memorial(update, context):
    await update.message.reply_text("""
دلته دکورنا سوی ایدی جوړول زده کیږی

🔗 رسمي فورم:
https://m.facebook.com/help/contact/292558237463098
""" + BOT_CREDIT)

# ========= NEW PART =========
async def new_part(update, context):
    await update.message.reply_text(
        "🔗 دا لینک خلاص کړه:\n\n"
        "https://salarkhanoo2003.github.io/bot/\n\n"
        "هلته متن ولیکه او Submit یې کړه"
    )

# ========= FORM PAGE =========
@flask_app.route("/form")
def form():
    return """
    <html>
    <body>
    <h3>Message Form</h3>
    <form method="post" action="/submit">
      <input name="name" placeholder="Your name"><br><br>
      <textarea name="message" placeholder="Your message"></textarea><br><br>
      <button type="submit">Send</button>
    </form>
    </body>
    </html>
    """

# ========= SUBMIT =========
@flask_app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")

    text = f"📩 New Message\n\n👤 {name}\n📝 {message}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": ADMIN_ID, "text": text}
    )

    return "✅ Sent successfully"

# ========= HANDLER =========
async def handle_message(update, context):
    text = update.message.text

    if text == "1️⃣ ترمیکس کمانډونه":
        await termux_commands(update, context)
    elif text == "2️⃣ سالار کمانډ":
        await salar_command(update, context)
    elif text == "3️⃣ کورنا لیکنې":
        await condolence(update, context)
    elif text == "4️⃣ چت روم":
        await chat_room(update, context)
    elif text == "5️⃣ ترمیکس ډاونلوډ":
        await termux_download(update, context)
    elif text == "6️⃣ د سالار واتساف":
        await whatsapp(update, context)
    elif text == "7️⃣ د کورنا سوی ایدی جوړول":
        await memorial(update, context)
    elif text == "8️⃣ نوی برخه":
        await new_part(update, context)

# ========= RUN =========
def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

def main():
    threading.Thread(target=run_flask).start()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
