import telebot
import time
import threading

TOKEN = 8381181264:AAE95B3hJENM0mkSHJupQq-VY6hkEtaTdaM
CHANNEL_ID = -1003789323635

bot = telebot.TeleBot(TOKEN)

def send_post(message):
    text = message.text
    if "t.me/c/" in text:
        try:
            post_id = int(text.split("/")[-1])
            msg = bot.copy_message(message.chat.id, CHANNEL_ID, post_id)
            
            # Delete after 20 minutes
            def delete_msg():
                time.sleep(1200)
                try:
                    bot.delete_message(message.chat.id, msg.message_id)
                except:
                    pass  # Agar already deleted ho gaya ho

            threading.Thread(target=delete_msg).start()
        except Exception as e:
            bot.reply_to(message, f"Post nahi mila ❌\nError: {e}")

@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    send_post(message)

print("Bot started… ✅")
bot.infinity_polling()
