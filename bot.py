import telebot
import time
import threading
import json

TOKEN = "8153911184:AAFeWlRNxbf-yD_oWyMCuWVMorZR6dRngpo"
BOT_USERNAME = "Ghopghop842_bot"
FORCE_CHANNEL = "https://t.me/+wN3r1YQoPAZkMzY1"

bot = telebot.TeleBot(TOKEN)

# user database
try:
    with open("users.json","r") as f:
        users = json.load(f)
except:
    users = []


def save_users():
    with open("users.json","w") as f:
        json.dump(users,f)


def delete_after(chat_id, msg_id):
    time.sleep(1200)
    try:
        bot.delete_message(chat_id,msg_id)
    except:
        pass


def check_join(user_id):
    try:
        status = bot.get_chat_member(FORCE_CHANNEL,user_id).status
        if status in ["member","administrator","creator"]:
            return True
    except:
        return False


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    if user_id not in users:
        users.append(user_id)
        save_users()

    if not check_join(user_id):
        bot.send_message(
            message.chat.id,
            f"⚠️ Pehle channel join karo\n\n{FORCE_CHANNEL}"
        )
        return

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
                args=(message.chat.id,msg.message_id)
            ).start()

        except:
            bot.send_message(message.chat.id,"⚠️ Post nahi mila")

    else:

        bot.send_message(
            message.chat.id,
            f"🤖 Bot Online Hai\n\n👥 Users: {len(users)}\n\nChannel post link bhejo"
        )


@bot.message_handler(func=lambda m: True)
def link_gen(message):

    if "t.me/c/" in message.text:

        try:

            parts = message.text.split("/")
            channel = parts[-2]
            post = parts[-1]

            channel_id = "-100" + channel

            link = f"https://t.me/{BOT_USERNAME}?start={channel_id}_{post}"

            bot.send_message(
                message.chat.id,
                f"✅ Bot Link:\n\n{link}"
            )

        except:

            bot.send_message(message.chat.id,"⚠️ Link galat hai")

    else:

        bot.send_message(message.chat.id,"❌ Channel post link bhejo")


print("Bot started...")
bot.infinity_polling()
