import os
import time
import uuid
from flask import Flask, request, render_template_string
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import asyncio
import threading

# ================== CONFIG ==================
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Railway Variable
ADMIN_ID = 5887665463

BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"
BASE_URL = "https://salarbot-production.up.railway.app"

USER_TOKENS = {}  # token: (user_id, expiry)

# ================== FLASK ==================
app = Flask(__name__)

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Salar Bot Form</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="font-family:sans-serif; padding:20px;">
    <h2>✍️ خپل متن ولیکه</h2>
    <form method="POST">
        <textarea name="text" rows="6" style="width:100%;" placeholder="دلته خپل متن ولیکه..." required></textarea>
        <br><br>
        <button type="submit" style="padding:10px 20px;">📤 واستوه</button>
    </form>
</body>
</html>
"""

@app.route("/form", methods=["GET", "POST"])
def form():
    token = request.args.get("token")
    if token not in USER_TOKENS:
        return "❌ لینک ناسم یا ختم شوی"

    user_id, expiry = USER_TOKENS[token]
    if time.time() > expiry:
        return "❌ لینک وخت ختم شوی"

    if request.method == "POST":
        text = request.form.get("text")
        asyncio.run(send_to_telegram(user_id, text))
        return "✅ متن بوت ته ولېږل شو، Telegram ته لاړ شه"

    return render_template_string(FORM_HTML)

# ================== TELEGRAM SEND ==================
async def send_to_telegram(user_id, text):
    await bot_app.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 نوی متن:\n\n{text}"
    )
    await bot_app.bot.send_message(
        chat_id=user_id,
        text=f"✅ ستا متن ترلاسه شو:\n\n{text}"
    )

# ================== TELEGRAM BOT ==================
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

async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = uuid.uuid4().hex
    USER_TOKENS[token] = (update.message.from_user.id, time.time() + 86400)

    link = f"{BASE_URL}/form?token={token}"

    await update.message.reply_text(
        "🔗 دا ستا شخصي لینک دی (۲۴ ساعته معتبر):\n\n"
        f"{link}\n\n"
        "هر براوزر کې یې خلاص کړه، متن ولیکه، او واستوه ✅"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "8️⃣ نوی برخه":
        await demo_page(update, context)
    else:
        await update.message.reply_text("ℹ️ مهرباني وکړئ له مینو څخه انتخاب وکړئ")

# ================== RUN BOT ==================
async def run_bot():
    global bot_app
    bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await bot_app.run_polling()

def start_all():
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080)).start()
    asyncio.run(run_bot())

if __name__ == "__main__":
    start_all()
