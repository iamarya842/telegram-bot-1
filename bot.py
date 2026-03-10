import telebot
import time
import threading

TOKEN = "8153911184:AAFeWlRNxbf-yD_oWyMCuWVMorZR6dRngpo"
BOT_USERNAME = "Ghopghop842_bot"

bot = telebot.TeleBot(TOKEN)


def delete_after(chat_id, msg_id):
    time.sleep(1200)  # 20 minutes
    try:
        bot.delete_message(chat_id, msg_id)
    except:
        pass


@bot.message_handler(commands=['start'])
def start(message):

    args = message.text.split()

    if len(args) > 1:
        try:
            data = args[1].split("_")

            channel_id = int(data[0])
            post_id = int(data[1])

            msg = bot.copy_message(
                message.chat.id,
                channel_id,
                post_id
            )

            threading.Thread(
                target=delete_after,
                args=(message.chat.id, msg.message_id)
            ).start()

        except:
            bot.send_message(message.chat.id, "⚠️ Post nahi mila")

    else:
        bot.send_message(message.chat.id, "🤖 Bot Online Hai\n\nChannel post link bhejo")


@bot.message_handler(func=lambda m: True)
def link_gen(message):

    if "t.me/c/" in message.text:
        try:
            parts = message.text.split("/")
            channel = parts[-2]
            post = parts[-1]

            channel_id = "-100" + channel

            link = f"https://t.me/{BOT_USERNAME}?start={channel_id}_{post}"

            bot.send_message(message.chat.id, f"✅ Bot Link:\n\n{link}")

        except:
            bot.send_message(message.chat.id, "⚠️ Link galat hai")

    else:
        bot.send_message(message.chat.id, "❌ Channel post link bhejo")


print("Bot started...")
bot.infinity_polling()
