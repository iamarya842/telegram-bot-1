import telebot
import time
import threading

TOKEN = "8153911184:AAFeWlRNxbf-yD_oWyMCuWVMorZR6dRngpo"
CHANNEL_ID = -1003789323635

bot = telebot.TeleBot(TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Bot Online Hai\n\nChannel post link bhejo.")

# Handle messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        text = message.text.strip()

        if "t.me/c/" in text:
            post_id = int(text.split("/")[-1])

            msg = bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=post_id
            )

            # Auto delete
            def auto_delete():
                time.sleep(1200)
                try:
                    bot.delete_message(message.chat.id, msg.message_id)
                except:
                    pass

            threading.Thread(target=auto_delete).start()

        else:
            bot.reply_to(message, "❌ Channel post link bhejo.")

    except Exception:
        bot.reply_to(message, "⚠️ Post nahi mila.")

print("Bot started...")
bot.infinity_polling()
