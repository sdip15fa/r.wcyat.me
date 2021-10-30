import logging
import os

import telegram
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import wcyatfiles as files

os.system(
    "git pull origin master && git pull azure master && pip install python-telegram-bot"
)

bottoken = str(os.environ["bottoken"])
owner = str(os.environ["owner"])
bot = telegram.Bot(token=bottoken)
updater = Updater(token=bottoken, use_context=True)
dispatcher = updater.dispatcher


def push():
    os.system("./push.sh")


def list(update, context):
    if str(update.effective_chat.id) == owner:
        o = ""
        try:
            os.system("rm tree.txt")
        except:
            pass
        os.system("tree > tree.txt")
        file = open("tree.txt")
        for line in file:
            o += line
        bot.send_message(chat_id=owner, text=o)
    else:
        bot.send_message(chat_id=update.effective_chat.id,
                         text="permission denied")


def create(dir, link, update, context):
    os.system("mkdir -p " + dir + " && cd " + dir + " && touch index.html")
    if files.checkexist(dir + "/index.html"):
        os.remove(dir + "/index.html")
    files.appendfile(
        dir + "/index.html",
        '<!DOCTYPE html><html lang="en-US"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0; url='
        + link + '" /></head><body></body></html>',
    )
    push()
    context.bot.send_message(chat_id=owner, text="Done.")


def remove(dir, update, context):
    try:
        os.system("rm -rf " + dir)
        push()
        context.bot.send_message(chat_id=owner, text="Done.")
    except:
        context.bot.send_message(chat_id=owner, text="No such path.")


def start(update, context):
    user = update.effective_chat.id
    cout = context.bot.send_message
    if str(user) == owner:
        cout(
            chat_id=owner,
            text="Commands:\n/create <path> <link>: create new redirect path\n/rm <path>: remove a redirect path\n/list: list files",
        )
    else:
        cout(chat_id=user, text="permission denied")


def messageh(update, context):
    if str(update.effective_chat.id) != owner:
        bot.send_message(chat_id=update.effective_chat.id,
                         text="permission denied")
    elif "/create" in update.message.text:
        i = 8
        path = ""
        while update.message.text[i] != " ":
            path += update.message.text[i]
            i += 1
        link = update.message.text.replace("/create " + path + " ", "")
        create(path, link, update, context)
    elif "/rm" in update.message.text:
        path = update.message.text.replace("/rm ", "")
        remove(path, update, context)


start_handler = CommandHandler("start", start)
list_handler = CommandHandler("list", list)
message_handler = MessageHandler(Filters.text, messageh)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(list_handler)
dispatcher.add_handler(message_handler)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
updater.start_polling()
