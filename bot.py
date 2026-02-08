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

# ========= BOT CREDIT =========
BOT_CREDIT = "🤖 دا بوټ د سالار خانو لخوا جوړ شوی"

# ========= TOKEN =========
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"

# ========= ADMIN ID =========
ADMIN_ID = 5887665463

# ========= SERVER URL (Flask) =========
SERVER_FORM_URL = "https://YOUR-SERVER-DOMAIN/form"

# ========= TOKEN STORE =========
USER_TOKENS = {}   # token: expiry_time

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

# ========= SALAR COMMAND =========
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
    await update.message.reply_text("🕊️ کورنا لیکنې موجودې دي")

# ========= CHAT ROOM =========
async def chat_room(update, context):
    await update.message.reply_text(
        "💬 چت روم:\n\n"
        "سلام زه سالار خانو یم، ستاسو نوم څه دی؟\n"
        "زه هر وخت قهرمان یم 🇦🇫\n"
        "زه کندهاری یم، ته د کوم ځای یې؟\n"
        "هر ځای سالار زنداباد ✌️"
    )

# ========= TERMUX DOWNLOAD =========
async def termux_download(update, context):
    await update.message.reply_text("""
📥 Termux Download Links:

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
دلته دکورنا سوی ایدی جوړول زده کیږی داسنادو سره

📌 لازم معلومات:
1️⃣ مکمل نوم
2️⃣ جیمیل
3️⃣ د پیدایښت تاریخ
4️⃣ اسناد

🔗 رسمي فورم:
https://m.facebook.com/help/contact/292558237463098
""" + BOT_CREDIT)

# =========================
# 🔴 نوی برخه (اصلاح شوی)
# =========================
async def demo_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = uuid.uuid4().hex
    USER_TOKENS[token] = time.time() + 86400   # 24 ساعته

    link = f"{SERVER_FORM_URL}?token={token}"

    await update.message.reply_text(
        "🔗 دا ستاسو شخصي لینک دی (۲۴ ساعته معتبر):\n\n"
        f"{link}\n\n"
        "هر براوزر کې یې خلاص کړه او فورم ډک کړه.\n"
        "متن به مستقیم بوت ته راشي ✅"
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
        await demo_page(update, context)
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
