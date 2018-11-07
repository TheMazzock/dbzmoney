from twx.botapi import TelegramBot, ReplyKeyboardMarkup

bot = TelegramBot('<API TOKEN>')
bot.update_bot_info().wait()
print(bot.username)

updates = bot.get_updates().wait()
for update in updates:
    print(update)
