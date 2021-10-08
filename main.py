import os, logging, telegram
import wcyatfiles as files
os.system("git pull origin master && pip install python-telegram-bot")
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
bottoken=str(os.environ['bottoken'])
owner = str(os.environ['owner'])
bot = telegram.Bot(token=bottoken)
updater = Updater(token=bottoken, use_context=True)
dispatcher = updater.dispatcher
def push():
  os.system("./push.sh")
def create(dir, link, update, context):
  os.system("mkdir " + dir + " && cd " + dir + " && touch index.html")
  if files.checkexist(dir + "/index.html"):
    os.remove(dir + "/index.html")
  files.appendfile(dir + "/index.html", "<html><body onload=\"window.location.href=\'" + link + "\'></body></html>")
  push()
  context.bot.send_message(chat_id=update.effective_user.id, text="Done.")
def remove(dir, update, context):
  os.system("rm -rf " + dir)
  push()
  context.bot.send_message(chat_id=update.effective_user.id, text="Done.")
def start(update, context):
  user = update.effective_user.id
  cout = context.bot.send_message
  if str(user) == owner:
    cout(chat_id=owner, text="Commands:\n/create <path> <link>: create new redirect path\n/rm <path>: remove a redirect path")
  else:
    cout(chat_id=user, text="permission denied")
def messageh(update, context):
  if str(update.effective_user.id) != owner:
    bot.send_message(chat_id=update.effective_user.id, text="permission denied")
  elif "/create" in update.message.text:
    i = 8
    path = ""
    while update.message.text[i] != " ":
      path += update.message.text[i]
      i += 1
    link = update.message.text.replace("/create " + path + " ", "")
    create(path, link, update, context)
  elif "/rm" in update.message.text:
    i = 4
    path = ""
    while update.message.text[i] != " ":
      path += update.message.text[i]
      i += 1
    remove(path, update, context)
start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, messageh)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater.start_polling()
