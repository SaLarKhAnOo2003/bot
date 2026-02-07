import json
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ================= CONFIG =================
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
ADMIN_ID = 5887665463   # خپل Telegram ID
WEBAPP_URL = "https://salarkhanoo2003.github.io/bot/"
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"
# =========================================

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["1️⃣ ترمیکس کمانډونه"],
        ["2️⃣ سالار کمانډ"],
        ["3️⃣ کورنا لیکنې"],
        ["4️⃣ چت روم"],
        ["5️⃣ ترمیکس ډاونلوډ"],
        ["6️⃣ د سالار واتساف"],
        ["7️⃣ د کورنا سوی ایدی جوړول"],
        [KeyboardButton("8️⃣ نوی برخه", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]

    await update.message.reply_text(
        f"سلام 👋\nیو انتخاب وکړئ 👇\n\n{BOT_CREDIT}",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# TERMUX COMMANDS
async def termux_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
pkg update
pkg upgrade
pkg install python
pkg install git
pip install requests mechanize bs4 rich
termux-setup-storage
""")

# SALAR COMMAND
async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
rm -rf SALAR
git clone https://github.com/SaLarKhAnOo2003/SALAR.git
cd SALAR
python SALAR.py
""")

# CONDOLENCE
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕊️ کورنا لیکنې موجودې دي")

# CHAT ROOM
async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام، زه سالار یم ✌️")

# TERMUX DOWNLOAD
async def termux_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://f-droid.org/packages/com.termux/"
    )

# WHATSAPP
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

# MEMORIAL
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دلته د کورنا سوی ایدی جوړولو معلومات دي\n\n"
        "https://m.facebook.com/help/contact/292558237463098"
    )

# RECEIVE WEBAPP DATA
async def webapp_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.effective_message.web_app_data.data)

    demo1 = data.get("demo1", "")
    demo2 = data.get("demo2", "")

    sender = update.effective_user

    text = (
        "📘 Demo Result\n\n"
        f"👤 Name: {sender.first_name}\n"
        f"🆔 ID: {sender.id}\n\n"
        f"Demo 1:\n{demo1}\n\n"
        f"Demo 2:\n{demo2}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("✅ متنونه واستول شول")

# MESSAGE HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    else:
        await update.message.reply_text("❌ له مینو انتخاب وکړه")

# MAIN
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
