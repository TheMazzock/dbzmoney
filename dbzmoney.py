from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1eLcpU6Sdguki_IJ7AUZVbbPJtSNSVW7DnCxDKX5u83l'
SAMPLE_RANGE_NAME = 'DC!A1:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    main()


"""
from telegram.ext import Updater, CommandHandler
from os import environ
from uuid import uuid4


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
"""
    
"""    
def put(bot, update, user_data): """
    """ Usage: /put value""" """
    # Generate ID and seperate value from command
    key = str(uuid4())
    value = update.message.text.partition(' ')[2]

    # Store value
    user_data[key] = value

    update.message.reply_text(key)
    
    
def get(bot, update, user_data):"""
    """Usage: /get uuid""" """
    # Seperate ID from command
    key = update.message.text.partition(' ')[2]

    # Load value
    try:
        value = user_data[key]
        update.message.reply_text(value)

    except KeyError:
        update.message.reply_text('Not found')    

def db_inserimento(bot, update):
    testo = update.message.text[15:]
    print(testo)
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')
dispatcher = updater.dispatcher

# LISTA DEI COMANDI
hello_handler = CommandHandler('hello', hello)
db_inserimento_handler = CommandHandler('db_inserimento', db_inserimento)
put_handler = CommandHandler('put', put, pass_user_data=True)
get_handler = CommandHandler('get', get, pass_user_data=True)


# LISTA DEI TESTI



# LISTA DEI PULSANTI

if __name__ == '__main__':
    updater = Updater('783761569:AAFk4MtxJkw0PmIsQf1uUfMYCo0wGLfsFSA')
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(db_inserimento_handler)
    dispatcher.add_handler(put_handler)
    dispatcher.add_handler(get_handler)
    updater.start_polling()
    updater.idle()
"""

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
