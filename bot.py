from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import requests

# ========= CREDIT =========
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"

# ========= TOKEN =========
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"

# ========= Railway Domain =========
RAILWAY_DOMAIN = "https://YOUR-RAILWAY-DOMAIN"  # مثال: https://salarbot-production.up.railway.app

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

# ========= OTHER PARTS (هماغه ستا پخواني) =========
async def termux_commands(update, context):
    await update.message.reply_text("📌 Termux Commands:\npkg update\npkg upgrade")

async def salar_command(update, context):
    await update.message.reply_text("📌 Salar Command:\ngit clone SALAR")

async def condolence(update, context):
    await update.message.reply_text("🕊️ کورنا لیکنې")

async def chat_room(update, context):
    await update.message.reply_text("💬 چت روم")

async def termux_download(update, context):
    await update.message.reply_text("📥 Termux Download Links")

async def whatsapp(update, context):
    await update.message.reply_text("💬 WhatsApp Group")

async def memorial(update, context):
    await update.message.reply_text("📌 د کورنا سوی ایدی جوړول")

# ========= 8️⃣ نوی برخه (لینک اخیستل) =========
async def new_part(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    # Flask نه لینک اخلو
    r = requests.get(f"{RAILWAY_DOMAIN}/generate", params={"user_id": user_id})
    link = r.text

    await update.message.reply_text(
        f"🔗 دا ستاسو شخصي لینک دی (۲۴ ساعته معتبر):\n\n{link}\n\n"
        "هر براوزر کې یې خلاص کړه او متن ولیکه."
    )

# ========= MESSAGE HANDLER =========
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
    else:
        await update.message.reply_text("❌ مهرباني وکړئ له مینو څخه انتخاب وکړئ")

# ========= MAIN =========
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
