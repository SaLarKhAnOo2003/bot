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
async def salar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📌 Salar Command:

rm -rf SALAR
git clone --depth=1 https://github.com/SaLarKhAnOo2003/SALAR.git
cd SALAR
python SALAR.py
""")

# ========= CONDOLENCE =========
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🕊️ کورنا لیکنې:

1️⃣

The news of your death came to my ears like a gun shot😭. He died during the bomb blast in Palestine 🇰🇼 R.I.P bro @  you will be in our hearts forever😭💔 pls remember my brother's account
Date of Death 21/10/2025 Time 12:55 AM
---------------------------------------------------

2️⃣

() May your soul rest in peace and may God bless you with paradise. 
I miss you so much. I see your Facebook messages every day. Every time I see your message, I cry.
My Facebook friend was a soldier in the country of afghanistan who.😭May the soul of those killed by Hamas group rest in peace😭😓💔
Dead Time 9:33 am 
Dead Date 13/7/2024
---------------------------------------------------

3️⃣

(@) was my best friends😭❤️‍🔥 He died yesterday. May god give him heaven, Rest in peace my brother. We will miss you so much. May god give strength to your family to accept this sad truth. I request to facebook so they make his account memorialize, as everyone can pray for him.🤚🏽😭💔
Rip my bro🌹🕊
---------------------------------------------------

4️⃣
Hello dear sir. Our soul is not permanent for living here but i am very sorry about my loss. My friend () has been died due to heart attack. He was well wisher for all humanity. I have never seen suck a kind person pls Facebook team help us to make memo my lovely friend's account. 
Pls give hearts prays and many memories to my dear..
Rest in peace 🕊️ dear 😭
---------------------------------------------------

5️⃣

I'm still in shock and disbelief that my best friend ( ) 💔😭 is gone. The pain of losing you is unbearable I miss you every second of every day I wish I could turn back the time and save you😭💐. rest in peace😭💐🕊️
Death date 22/1/2025 time 11:30pm
---------------------------------------------------
""")

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
    await update.message.reply_text("""
📥 Termux Download Links:

1️⃣ https://f-droid.org/packages/com.termux/
---------------------------------------------------
2️⃣ https://github.com/termux/termux-app/releases
---------------------------------------------------
3️⃣ https://apkpure.com/termux/com.termux
---------------------------------------------------
4️⃣ https://apkcombo.com/termux/com.termux/
---------------------------------------------------
5️⃣ https://uptodown.com/android/termux
---------------------------------------------------
""")

# ========= WHATSAPP =========
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 WhatsApp Group:\n\n"
        "https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV"
    )

# ========= MEMORIAL =========
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
دلته دکورنا سوی ایدی جوړول زده کیږی داسنادو سره

📌 لازم معلومات:
1️⃣ د مړ شوي کس بشپړ نوم
2️⃣ دوهم دمر سوی شخص جیمیل
3️⃣ دمری سوی شخص داسنادو دفیدایشت نیته
4️⃣ دمر سوی شخص اسناد یادونه دفیدایشت نیته باید داسنادو فه رکم یی  او دایدی نوم او فیدایشت نیته هم باید داسنادو فه رکم وی


🔗 د فیسبوک رسمي فورم:
https://m.facebook.com/help/contact/292558237463098

ℹ️ یادونه:
دا لینګ یوازی دکورنا سوی ایډی جوړولو لپاره کارکوی 

""" + BOT_CREDIT)

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
