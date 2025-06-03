import telebot
import os

BOT_TOKEN = os.getenv("8144884790:AAFY1nwHQi5HAl5n5YTkY6IAscmlPf7ajJA")  # set this in Render Environment tab

bot = telebot.TeleBot(8144884790:AAFY1nwHQi5HAl5n5YTkY6IAscmlPf7ajJA)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👻 Yo, I’m Ghost AI — always watching you 👀.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()

    if "hi" in text or "hello" in text:
        reply = "Yo! What’s cracking, legend?"
    elif "stupid" in text:
        reply = "Careful, champ — your brain might be on low battery."
    elif "beef" in text:
        reply = "I’m the butcher, and you’re next on the grill 🔪🥩."
    elif "how are you" in text:
        reply = "Vibing at 110%, you?"
    elif "idiot" in text:
        reply = "Easy soldier — don’t throw what you can’t catch."
    elif "your father" in text:
        reply = "Leave my old man outta this 😆."
    elif "love" in text:
        reply = "Awww... love is a scam but I’ll allow it 💔."
    elif "money" in text:
        reply = "If money talks, mine sings Afrobeats 🤑🎶."
    elif "fine" in text:
        reply = "Born fine, living finer 😎."
    elif "crazy" in text:
        reply = "You ain't seen crazy till you meet my Monday mornings."
    elif "who are you" in text:
        reply = "I’m the ghost in your machine. The legend you can’t mute."
    else:
        reply = "Say less. I’m watching you like a hawk on night patrol 👀."

    bot.reply_to(message, reply)

# Start polling
bot.infinity_polling()
