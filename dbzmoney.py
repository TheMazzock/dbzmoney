import sys, traceback
from time import sleep
from twx.botapi import TelegramBot, ReplyKeyboardMarkup

TOKEN = '783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA'

bot = TelegramBot(TOKEN)
bot.update_bot_info().wait()
print(bot.username)
last_update_id = 0
    

def process_message(bot, u):
    keyboard = [['Ciao']]
    reply_markup = ReplyKeyboardMarkup.create(keyboard)
    if u.message.sender and u.message.text and u.message.chat:
        chat_id = u.message.chat.id
        user = u.message.sender.username
        message = u.message.text
        print(chat_id)
        print(user)
        print(message)
        if message == 'Ciao':
            dainviare = 'Ciao è un piacere conoscerti, ' + user
            bot.send_message(chat_id, 'Ciao è un piacere conoscerti,')
        else:
            bot.send_message(chat_id, 'please select an option', reply_markup=reply_markup).wait()
        
        
        
while True:
    updates = bot.get_updates(offset = last_update_id).wait()
    print(updates)
    try:
        for update in updates:
            if int(update.update_id) > int(last_update_id):
                last_update_id = update.update_id
                process_message(bot, update)
                continue
        continue
    except Exception:
        ex = None
        print(traceback.format_exc())
        continue
