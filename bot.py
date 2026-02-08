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

# ========= ADMIN ID =========
ADMIN_ID = 5887665463

# ========= LAST REQUESTER =========
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


# ========= TERMUX =========
async def termux_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "pkg update\npkg upgrade\npkg install python\npkg install git\n"
        "pip install requests\npip install mechanize\npip install bs4 futures\n"
        "pip install rich\ntermux-setup-storage\npip install pycurl"
    )


async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "rm -rf SALAR\n"
        "git clone --depth=1 https://github.com/SaLarKhAnOo2003/SALAR.git\n"
        "cd SALAR\npython SALAR.py"
    )


async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕊️ کورنا لیکنې موجودې دي...")


async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💬 سلام! زه سالار خانو یم 👋")


async def termux_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://f-droid.org/packages/com.termux/\n"
        "https://github.com/termux/termux-app/releases"
    )


async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )


async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 https://m.facebook.com/help/contact/292558237463098\n\n" + BOT_CREDIT
    )


# =========================
# 🔴 NEW PART – REAL FORM LINK
# =========================
async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global LAST_REQUESTER_ID
    LAST_REQUESTER_ID = update.message.from_user.id

    keyboard = [[{
        "text": "📘 فورم خلاص کړه",
        "web_app": WebAppInfo(
            url="https://salarbot-production.up.railway.app/form"
        )
    }]]

    await update.message.reply_text(
        "دا ستا شخصي فورم دی (۲۴ ساعته معتبر) 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


# =========================
# 🔴 DATA FROM FORM
# =========================
async def webapp_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = json.loads(update.message.web_app_data.data)

    name = data.get("name", "")
    message = data.get("message", "")

    text = f"📩 New Form Data\n\n👤 {name}\n📝 {message}"

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
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
        await update.message.reply_text("❌ له مینو انتخاب وکړه")


# ========= MAIN =========
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()
