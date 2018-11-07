from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('saldo', 'sempre poco'))

updater.start_polling()
updater.idle()
