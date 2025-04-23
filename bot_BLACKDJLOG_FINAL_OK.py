import telebot
from flask import Flask, request
import os

API_TOKEN = "7838687843:AAGkLGQ3_G70f5pmP4H0w_dLRnHlA0xxtYY"
WEBHOOK_URL = "https://blackdjlog.onrender.com/webhook"

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "✅ BLACKDJLOG BOT IS LIVE"

@app.route("/webhook", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    print("📥 Telegram message reçu via /webhook")
    return "OK", 200

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "🔥 Bienvenue sur BLACKDJLOG ! Bot 100% en ligne.")

if __name__ == "__main__":
    print("🚀 Lancement de BLACKDJLOG")
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
