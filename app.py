from flask import Flask, request, render_template
import uuid, time, requests, os

app = Flask(__name__)

BOT_TOKEN = os.getenv("8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps")
TOKENS = {}

@app.route("/generate")
def generate():
    user_id = request.args.get("user_id")
    token = uuid.uuid4().hex
    TOKENS[token] = {
        "user": user_id,
        "exp": time.time() + 86400
    }
    return f"{request.host_url}form?token={token}"

@app.route("/form")
def form():
    token = request.args.get("token")
    if token not in TOKENS or time.time() > TOKENS[token]["exp"]:
        return "❌ لینک ختم شوی"
    return render_template("form.html", token=token)

@app.route("/submit", methods=["POST"])
def submit():
    token = request.form.get("token")
    text = request.form.get("text")

    if token not in TOKENS:
        return "❌ ناسم لینک"

    user_id = TOKENS[token]["user"]

    msg = f"📩 نوی متن:\n\n{text}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": user_id, "text": msg})

    return "✅ متن بریالی واستول شو"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
