import os
import json
from telegram import Update, ReplyKeyboardMarkup, WebAppInfo
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

# ========= ADMIN =========
ADMIN_ID = 5887665463
LAST_REQUESTER_ID = None


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


# ========= TERMUX COMMANDS =========
async def termux_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
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


# ========= SALAR COMMAND =========
async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
rm -rf SALAR
git clone --depth=1 https://github.com/SaLarKhAnOo2003/SALAR.git
cd SALAR
python SALAR.py
""")


# ========= CONDOLENCE =========
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕊️ کورنا لیکنې...")


# ========= CHAT ROOM =========
async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 چت روم...")


# ========= TERMUX DOWNLOAD =========
async def termux_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
https://f-droid.org/packages/com.termux/
https://github.com/termux/termux-app/releases
https://apkpure.com/termux/com.termux
https://apkcombo.com/termux/com.termux/
https://uptodown.com/android/termux
""")


# ========= WHATSAPP =========
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )


# ========= MEMORIAL =========
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "د کورنا سوی ایدی جوړول...\n\n"
        "https://m.facebook.com/help/contact/292558237463098\n\n"
        + BOT_CREDIT
    )


# ========= DEMO PAGE =========
async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global LAST_REQUESTER_ID
    LAST_REQUESTER_ID = update.message.from_user.id

    keyboard = [[{
        "text": "📘 Open Demo Page",
        "web_app": WebAppInfo(url="https://salarkhanoo2003.github.io/bot/")
    }]]

    await update.message.reply_text(
        "Demo Page خلاص کړه 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# ========= WEBAPP DATA =========
async def webapp_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.message.web_app_data.data)

    msg = f"""
📘 Demo Page Data

{data}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)
    await update.message.reply_text("✅ معلومات واستول شول")


# ========= MESSAGE HANDLER =========
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
    elif text == "8️⃣ نوی برخه":
        await demo_page(update, context)
    else:
        await update.message.reply_text("❌ له مېنو انتخاب وکړه")


# ========= MAIN =========
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
