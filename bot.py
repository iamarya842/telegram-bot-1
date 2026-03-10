import telebot

TOKEN = "8153911184:AAFeWlRNxbf-yD_oWyMCuWVMorZR6dRngpo"
CHANNEL_ID = -1003789323635   # apna channel id

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = message.text.split()

    if len(text) > 1:
        try:
            post_id = int(text[1])

            bot.copy_message(
                message.chat.id,
                CHANNEL_ID,
                post_id
            )

        except:
            bot.send_message(message.chat.id, "⚠️ Post nahi mila")

    else:
        bot.send_message(message.chat.id, "🤖 Bot Online Hai\n\nChannel post link bhejo")

@bot.message_handler(func=lambda message: True)
def generate_link(message):

    if "t.me/c/" in message.text:

        try:
            post_id = message.text.split("/")[-1]

            link = f"https://t.me/Ghopghop842_bot?start={post_id}"

            bot.send_message(
                message.chat.id,
                f"✅ Bot Link:\n\n{link}"
            )

        except:
            bot.send_message(message.chat.id, "⚠️ Link galat hai")

    else:
        bot.send_message(message.chat.id, "❌ Channel post link bhejo")

print("Bot started...")
bot.infinity_polling()
