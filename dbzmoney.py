from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')
dispatcher = updater.dispatcher

# LISTA DEI COMANDI
hello_handler = CommandHandler('hello', hello)


# LISTA DEI TESTI



# LISTA DEI PULSANTI


dispatcher.add_handler(hello_handler)

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
