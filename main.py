import os
import threading
from flask import Flask
import telebot

TOKEN = "8811762467:AAH-D1MxUHTXtZ3FtRLOLDSFYzIr3nuBP0"
bot = telebot.TeleBot(TOKEN)

app = Flask("")

@app.route("/")
def home():
    return "Bot is running and active!"

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي معرف تويتر (يوزرنيم) لأعرض لك معلومات الحساب.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.text.replace("@", "").strip()
    bot.reply_to(message, f"جاري البحث عن معلومات الحساب: @{username}\n(قريباً سيتم ربط جلب البيانات مباشرة).")

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    t = threading.Thread(target=run_flask)
    t.start()
    bot.infinity_polling()
