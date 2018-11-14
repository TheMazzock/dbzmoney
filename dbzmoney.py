from telegram.ext import Updater, CommandHandler
from os import environ


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def db_inserimento(bot, update):
    print(update)
    print('{}'.format(update.message.text)})
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')
dispatcher = updater.dispatcher

# LISTA DEI COMANDI
hello_handler = CommandHandler('hello', hello)
db_inserimento_handler = CommandHandler('db_inserimento', db_inserimento)


# LISTA DEI TESTI



# LISTA DEI PULSANTI


dispatcher.add_handler(hello_handler)
dispatcher.add_handler(db_inserimento_handler)

updater.start_polling()
updater.idle()

"""
class RegistrazioneContabile:
    def __init__(self, key, data, conto, importo, descrizione, personale, mese):
        self.key = key
        self.data = data
        self.conto = conto
        self.importo = importo
        self.descrizione = descrizione
        self.personale = personale
        self.mese = mese
    def crea_lista(self):
        return [self.key, self.data, self.conto, self.importo, self.descrizione, self.personale, self.mese]
    
"""
