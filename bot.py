import json
import uuid
import time
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ========= BOT INFO =========
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
ADMIN_ID = 5887665463
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"
WEBAPP_URL = "https://salarkhanoo2003.github.io/bot/index.html"

# ========= LINK STORAGE =========
USER_LINKS = {}  # token: expiry_time

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

# ========= MENU FUNCTIONS =========
async def termux_commands(update, context):
    await update.message.reply_text("""📌 Termux Commands:
pkg update
pkg upgrade
pkg install python
pkg install git
pip install requests mechanize bs4 rich
termux-setup-storage
""")

async def salar_command(update, context):
    await update.message.reply_text("""📌 Salar Command:
rm -rf SALAR
git clone https://github.com/SaLarKhAnOo2003/SALAR.git
cd SALAR
python SALAR.py
""")

async def condolence(update, context):
    await update.message.reply_text("🕊️ کورنا لیکنې\n\n(ستا هماغه پخوانی متن دلته محفوظ دی)")

async def chat_room(update, context):
    await update.message.reply_text(
        "💬 چت روم:\n"
        "سلام زه سالار خانو یم، ستاسو نوم څه دی؟\n"
        "زه کندهاری یم، ته د کوم ځای یې؟"
    )

async def termux_download(update, context):
    await update.message.reply_text("""📥 Termux Download:
https://f-droid.org/packages/com.termux/
https://github.com/termux/termux-app/releases
""")

async def whatsapp(update, context):
    await update.message.reply_text(
        "💬 WhatsApp Group:\nhttps://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

async def memorial(update, context):
    await update.message.reply_text("""📌 د کورنا سوی ایدی جوړول
لازم معلومات:
1️⃣ مکمل نوم
2️⃣ جیمیل
3️⃣ د پیدایښت تاریخ
4️⃣ اسناد

🔗 رسمي فورم:
https://m.facebook.com/help/contact/292558237463098
""" + BOT_CREDIT)

# ========= NEW PART (LINK SYSTEM) =========
async def new_part(update, context):
    token = uuid.uuid4().hex
    USER_LINKS[token] = time.time() + 86400  # 24 hours

    link = f"{WEBAPP_URL}?token={token}"

    await update.message.reply_text(
        "🔗 دا ستا شخصي لینک دی (۲۴ ساعته معتبر):\n\n"
        f"{link}\n\n"
        "لینک کاپي کړه، براوزر کې یې خلاص کړه او فورم ډک کړه."
    )

# ========= WEBAPP DATA =========
async def webapp_handler(update, context):
    try:
        data = json.loads(update.message.web_app_data.data)
    except:
        return

    token = data.get("token")
    name = data.get("name")
    message = data.get("message")

    if token not in USER_LINKS:
        await update.message.reply_text("❌ لینک ناسم دی")
        return

    if time.time() > USER_LINKS[token]:
        del USER_LINKS[token]
        await update.message.reply_text("❌ لینک ختم شوی")
        return

    del USER_LINKS[token]

    await context.bot.send_message(
        ADMIN_ID,
        f"📩 New Data\n\n👤 Name: {name}\n📝 Message:\n{message}"
    )

    await update.message.reply_text("✅ معلومات واستول شول")

# ========= TEXT HANDLER =========
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
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
