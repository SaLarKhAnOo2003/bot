import os
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
# ❗ دلته خپل توکن پیست کړه
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"

# ========= START =========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["1️⃣ ترمیکس کمانډونه"],
        ["2️⃣ سالار کمانډ"],
        ["3️⃣ کورنا لیکنې"],
        ["4️⃣ چت روم"],
        ["5️⃣ ترمیکس ډاونلوډ"],
        ["6️⃣ د سالار واتساف"],
        ["7️⃣ د کورنا سوی ایدی جوړول"]
    ]
    await update.message.reply_text(
        f"👋 سلام!\nیو انتخاب وکړئ 👇\n\n{BOT_CREDIT}",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# ========= TERMUX COMMANDS =========
async def termux_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Termux Commands:\n\n"
        "pkg update && pkg upgrade\n"
        "pkg install python git\n"
        "pip install requests mechanize bs4 rich\n"
        "termux-setup-storage"
    )

# ========= SALAR COMMAND =========
async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Salar Command:\n\n"
        "rm -rf SALAR\n"
        "git clone https://github.com/SaLarKhAnOo2003/SALAR.git\n"
        "cd SALAR\n"
        "python SALAR.py"
    )

# ========= CONDOLENCE =========
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕊️ کورنا لیکنې:\n\n"
        "1️⃣ Rest in peace my brother 💔😭\n"
        "2️⃣ May your soul rest in peace 🕊️\n"
        "3️⃣ Facebook team please memorialize this account\n"
        "4️⃣ We miss you forever 😭"
    )

# ========= CHAT ROOM =========
async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 چت روم:\n\n"
        "سلام زه سالار خانو یم، ستاسو نوم څه دی؟\n"
        "زه هر وخت قهرمان یم 🇦🇫\n"
        "زه کندهاری یم، ته د کوم ځای یې؟\n"
        "هر ځای سالار زنداباد ✌️"
    )

# ========= TERMUX DOWNLOAD =========
async def termux_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 Termux Download:\n\n"
        "https://f-droid.org/packages/com.termux/\n"
        "https://github.com/termux/termux-app/releases"
    )

# ========= WHATSAPP =========
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 WhatsApp Group:\n\n"
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

# ========= MEMORIAL =========
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕊️ د مړ شوي شخص Facebook Memorial\n\n"
        "لازم معلومات:\n"
        "1️⃣ بشپړ نوم\n"
        "2️⃣ ایمیل\n"
        "3️⃣ د اسنادو عکس\n\n"
        "🔗 فورم:\n"
        "https://www.facebook.com/help/contact/228813257197480\n\n"
        + BOT_CREDIT
    )

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
    else:
        await update.message.reply_text("❌ مهرباني وکړئ له مینو څخه انتخاب وکړئ")

# ========= MAIN =========
def main():
    if BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❌ مهرباني وکړئ BOT TOKEN داخل کړئ")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
