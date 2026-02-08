from flask import Flask, request, render_template, abort
import requests

app = Flask(__name__)

BOT_TOKEN = "8104728401:AAGnpTrjMUzkl6ddSEPHHtfgzjEcIhiLhps"
ADMIN_ID = 5887665463

@app.route("/form")
def form():
    token = request.args.get("token")
    if not token:
        abort(403)
    return render_template("index.html", token=token)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")

    if not name or not message:
        abort(400)

    text = f"📩 New Message\n\n👤 {name}\n📝 {message}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": ADMIN_ID, "text": text}
    )

    return "✅ معلومات واستول شول، مننه!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
