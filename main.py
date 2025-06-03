from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Replace this with your real Telegram Bot Token
BOT_TOKEN8144884790:AAFY1nwHQi5HAl5n5YTkY6IAscmlPf7ajJA"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👻 Yo, I'm Ghost Bot! Tell me how you feel.")

# Message handler
async def mood_reader(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "angry" in text:
        await update.message.reply_text("🔥 Chill boss, life's too short to be mad. Grab a cold drink.")
    elif "happy" in text:
        await update.message.reply_text("✨ Yooo, happiness looks good on you, don’t stop shining!")
    elif "sad" in text:
        await update.message.reply_text("💔 Tough days come, tough souls survive. You got this.")
    elif "confused" in text:
        await update.message.reply_text("🌀 When in doubt, take a deep breath. The answer’s inside.")
    else:
        await update.message.reply_text("👀 I'm feelin' that vibe. Hit me with a mood word: angry, happy, sad, confused.")

# Main app
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mood_reader))

    print("👻 Ghost AI Bot is live!")
    app.run_polling()

if __name__ == "__main__":
    main()
