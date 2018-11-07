from twx.botapi import TelegramBot, ReplyKeyboardMarkup

bot = TelegramBot('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')
bot.update_bot_info().wait()
print(bot.username)

updates = bot.get_updates().wait()
for update in updates:
    print(update)
