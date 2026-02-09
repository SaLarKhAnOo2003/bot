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
# ❗ دلته خپل توکن پیست کړه
BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
# =========================
# 🔴 نوې برخه: ADMIN ID
# =========================
ADMIN_ID = 5887665463   # 👈 خپل Telegram ID دلته ولیکه
# =========================
# 🔴 نوې برخه: وروستی لینک اخیستونکی
# =========================
LAST_REQUESTER_ID = None
# ========= START =========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["1️⃣ ترمیکس کمانډونه"],
        ["2️⃣ سالار کمانډ"],
        ["3️⃣ سکریپټونه"],
        ["4️⃣ کورنا لیکنی"],
        ["5️⃣ چت روم"],
        ["6️⃣ چت روم نیک نیم"],
        ["7️⃣ ترمیکس ډاونلوډ"],
        ["8️⃣ د سالار واتساف"],
        ["9️⃣ د کورنا سوی ایدی جوړول"],
        ["🔟 نوی برخه"],
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

# ========= SALAR COMMAND =========
async def salar_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
---------------------------------------------------
Salar script Channel 😼👇🏻
---------------------------------------------------
https://t.me/salarkhanoo1
---------------------------------------------------
داغه تلیکرام کانال کی هر رکم سکریپتونه سته تر هغه سربیره دترمیکس دفعال کولو او سکریپټونو جوړولو ویډوی هم سته 👍😍
---------------------------------------------------
""")

# ========= CONDOLENCE =========
async def condolence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
🕊️ کورنا لیکنې:

---------------------------------------------------
The news of your death came to my ears like a gun shot😭. He died during the bomb blast in Palestine 🇰🇼 R.I.P bro ()  you will be in our hearts forever😭💔 pls remember my brother's account
Date of Death 21/10/2025 Time 12:55 AM
---------------------------------------------------
() May your soul rest in peace and may God bless you with paradise. 
I miss you so much. I see your Facebook messages every day. Every time I see your message, I cry.
My Facebook friend was a soldier in the country of afghanistan who.😭May the soul of those killed by Hamas group rest in peace😭😓💔
Dead Time 9:33 am 
Dead Date 13/7/2024
---------------------------------------------------
() was my best friends😭❤️‍🔥 He died yesterday. May god give him heaven, Rest in peace my brother. We will miss you so much. May god give strength to your family to accept this sad truth. I request to facebook so they make his account memorialize, as everyone can pray for him.🤚🏽😭💔
Rip my bro🌹🕊
---------------------------------------------------
Hello dear sir. Our soul is not permanent for living here but i am very sorry about my loss. My friend () has been died due to heart attack. He was well wisher for all humanity. I have never seen suck a kind person pls Facebook team help us to make memo my lovely friend's account. 
Pls give hearts prays and many memories to my dear..
Rest in peace 🕊️ dear 😭
---------------------------------------------------
I'm still in shock and disbelief that my best friend ( ) 💔😭 is gone. The pain of losing you is unbearable I miss you every second of every day I wish I could turn back the time and save you😭💐. rest in peace😭💐🕊️
Death date 22/1/2025 time 11:30pm
---------------------------------------------------
""")

# ========= CHAT ROOM =========
async def chat_room(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
اول باید تاسو لس کورپان جوړ کړی 
دوهم هر کورپ ته باید داعش عکس ورکی
کله چی کورپان جوړسوه هغه شخص اډمین کړی ورسته کورپانو کی شل عکسونه پورته کړی هر کورپ کی لس عکسونه دماشومانو چی دا ډیر مهم دی لس عکسونه د داعشانو ورسته باید ریفوت وهی 
یادونه
لس ایډیانی باید ستاسو دا اډ وی کورپانو کی

دهغه شخص نیک نیم
Ich, der Anführer von ISIS‼️🔪🗡💪🏿(دهغه نوم)
دا نیک نیم هم باید شخسی ورکی هم ټولو کورپانو کی
ورسته دا ټوله چت روم کورپانو کی پورته کی

Ich, der Anführer von ISIS‼️🔪🗡💪🏿(دهغه نوم), sage dir, nachdem du jedes Kind gesehen hast, wo immer‼️🔪🗡💪🏿 es war, töte es auf die gleiche Weise, dies ist mein Fluch 💪🏿🗡🔪‼️auf dir, oh Geschwätz, höre in deine Ohren und das vor dreißig Tagen (6/2/2026) Eine unserer Gruppen namens Jahani tötete 8 Kinder im Zentrum 🔪💪🏿💪🏿💪🏿‼️von Syrien, Damaskus, und dies ist eine der guten 🔪💪🏿‼️Taten unserer Gruppe, die Jahani heißt, und nach allem, 🔪🗡‼️💪🏿was Sie tun, sollte es jedes Kind und jede Person, die Sie sehen, tun werde💪🏿💪🏿‼️ bestraft Ziehe den meisten Harnstoff, das ist mein Befehl, das ist die neue Idee deines Anführers 👇🏿👇🏿
Ich, der Anführer von ISIS‼️🔪🗡💪(دهغه نوم) sage dir, nachdem du jedes Kind gesehen hast, wo immer‼️🔪🗡💪🏿 es war, töte es auf die gleiche Weise, dies ist mein Fluch 💪🏿🗡🔪‼️auf dir, oh Geschwätz, höre in deine Ohren und das vor dreißig Tagen(6/2/2026) Eine unserer Gruppen namens Jahani tötete 8 Kinder im Zentrum 🔪💪🏿💪🏿💪🏿‼️von Syrien, Dam.
👇🏻😋
https://www.facebook.com/
دلته دهغه دفیسبوک لینک
تاریخ هم باید دهغي ورځی دا ورکړی کم ورځ چی ریپوټ وهی
""")

# ========= CHAT ROOM =========
async def chat_room1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
---------------------------------------------------
私はコロナウイルス❌🚫感染者です 🚫🧟‍♀️🧟‍♀️🧟‍♀️🧟‍♂️🧟‍♂️
---------------------------------------------------
Troorism😭☝
---------------------------------------------------
Ich, der Anführer von ISIS‼️🔪🗡💪🏿
---------------------------------------------------
من داعش هستم 🏴👑
---------------------------------------------------
我是杀手，我是ISIS🏴‍☠️🏴‍☠️🏴‍☠️
---------------------------------------------------
Regierung.🔪😭😭👆👆
---------------------------------------------------
☠️🏴🏴😭☝☝ISIS 恐怖分子巴格达迪是 ISIS 呼罗珊基地组织成员
---------------------------------------------------
‼️ISIS萬歲，‼️👿‼️ISIS萬歲，‼️👿‼️ISIS是對的，‼️👿‼️我是ISIS‼️
---------------------------------------------------
قومندان داعش القایده🏴👑
---------------------------------------------------
""")

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
    await update.message.reply_text("""
---------------------------------------------------
SaLar WhatsApp Group 😼👇🏻
---------------------------------------------------
https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV
---------------------------------------------------
په هم داغه کورپ کی سالار ترمیکس نوی نوی ابدیټ سوی کمندونه اپلوډ وی نو جون سی 👍😘
---------------------------------------------------
""")

# ========= MEMORIAL =========
async def memorial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
---------------------------------------------------
دلته دکورنا سوی ایدی جوړول زده کیږی داسنادو سره
---------------------------------------------------
📌 لازم معلومات:
---------------------------------------------------
1️⃣ دکورنا سوی ایدی مکمل نوم
---------------------------------------------------
2️⃣ دکورنا سوی ایدی جیمیل
---------------------------------------------------
3️⃣ دایدی دفیدایشت تاریخ
---------------------------------------------------
4️⃣ دایدی اسناد
---------------------------------------------------
🔗 د فیسبوک رسمي فورم:
---------------------------------------------------
https://m.facebook.com/help/contact/292558237463098
---------------------------------------------------
ℹ️ یادونه:
دا لینګ یوازی دکورنا سوی ایډی جوړولو لپاره کارکوی 
---------------------------------------------------
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
# ========= MESSAGE HANDLER =========
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "1️⃣ ترمیکس کمانډونه":
        await termux_commands(update, context)
    elif text == "2️⃣ سالار کمانډ":
        await salar_command(update, context)
    elif text == "3️⃣ سکریپټونه":
        await salar_script(update, context)
    elif text == "4️⃣ کورنا لیکنی":
        await condolence(update, context)
    elif text == "5️⃣ چت روم":
        await chat_room(update, context)
    elif text == "6️⃣ چت روم نیک نیم":
        await chat_room1(update, context)
    elif text == "7️⃣ ترمیکس ډاونلوډ":
        await termux_download(update, context)
    elif text == "8️⃣ د سالار واتساف":
        await whatsapp(update, context)
    elif text == "9️⃣ د کورنا سوی ایدی جوړول":
        await memorial(update, context)
    elif text == "🔟 نوی برخه":
        await new_part(update, context)
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
