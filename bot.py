import json
import uuid
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

# ========= CONFIG =========
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
ADMIN_ID = 5887665463
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"
WEBAPP_BASE_URL = "https://salarkhanoo2003.github.io/bot/"
# ==========================

# یو ځل کارېدونکي tokenونه
USED_TOKENS = set()

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
        "pkg update\npkg upgrade\npkg install python git\npip install requests mechanize bs4 rich\ntermux-setup-storage"
    )

# ========= SALAR =========
async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "rm -rf SALAR\n"
        "git clone --depth=1 https://github.com/SaLarKhAnOo2003/SALAR.git\n"
        "cd SALAR\npython SALAR.py"
    )

# ========= CONDOLENCE =========
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🕊️ کورنا لیکنې موجودې دي")

# ========= CHAT =========
async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام، زه سالار یم ✌️")

# ========= TERMUX DL =========
async def termux_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://f-droid.org/packages/com.termux/")

# ========= WHATSAPP =========
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

# ========= MEMORIAL =========
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دلته د کورنا سوی ایدی جوړولو معلومات دي:\n"
        "https://m.facebook.com/help/contact/292558237463098\n\n"
        + BOT_CREDIT
    )

# ========= یو ځل‌کارېدونکی لینک =========
def generate_one_time_link():
    token = uuid.uuid4().hex
    link = f"{WEBAPP_BASE_URL}?token={token}"
    return link, token

# ========= نوی برخه =========
async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link, token = generate_one_time_link()

    keyboard = [[
        KeyboardButton(
            text="🔓 دلته کلیک وکړه او متن واستوه",
            web_app=WebAppInfo(url=link)
        )
    ]]

    await update.message.reply_text(
        "🔗 دا ستاسو لینک دی (یو ځل کارېدونکی):\n\n"
        f"{link}\n\n"
        "📌 لینک هر څوک خلاصولی شي\n"
        "📩 خو متن یوازې یو ځل قبولېږي 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# ========= WEBAPP DATA =========
async def webapp_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.web_app_data:
        return

    data = json.loads(update.message.web_app_data.data)
    token = data.get("token")

    if not token:
        await update.message.reply_text("❌ نامعتبر لینک")
        return

    if token in USED_TOKENS:
        await update.message.reply_text("❌ دا لینک مخکې کارول شوی")
        return

    USED_TOKENS.add(token)

    field1 = data.get("field1", "")
    field2 = data.get("field2", "")

    text = (
        "📘 One-Time WebApp Data\n\n"
        f"🔐 Token:\n{token}\n\n"
        f"Field 1:\n{field1}\n\n"
        f"Field 2:\n{field2}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("✅ معلومات ثبت شول (لینک مصرف شو)")

# ========= MESSAGE ROUTER =========
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
        await update.message.reply_text("❌ مهرباني وکړئ له مینو څخه انتخاب وکړئ")

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
