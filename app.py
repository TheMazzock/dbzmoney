import os
from flask import Flask, render_template
import googleapiclient.discovery
from google.oauth2 import service_account
import telepot, time, sqlite3, random, csv
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint

def get_credentials():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = os.environ["GOOGLE_PRIVATE_KEY"]
    # The environment variable has escaped newlines, so remove the extra backslash
    GOOGLE_PRIVATE_KEY = GOOGLE_PRIVATE_KEY.replace('\\n', '\n')

    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }

    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials


def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service

service = get_service()
spreadsheet_id = os.environ["GOOGLE_SPREADSHEET_ID"]
range_name = "database!B1:B100"
result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])
print(values)


start_keyboard = [["Situazione","Conti del mese"],["Inserisci"],["Aiuto"]]
start_markup = ReplyKeyboardMarkup(keyboard=start_keyboard, one_time_keyboard=False)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Situazione', callback_data='situazione'),
                     InlineKeyboardButton(text='Conti', callback_data='conti')],
                     [InlineKeyboardButton(text='Inserimento', callback_data='inserimento')],
                 ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == "situazione":
        bot.answerCallbackQuery(query_id, text='Situazione patrimonio aggiornata')
    elif query_data == "conti":
        bot.answerCallbackQuery(query_id, text='Situazione conti aggiornata')
    elif query_data == "inserimento":
        bot.answerCallbackQuery(query_id, text='Pronto ad inserire!')


"""
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    
    try:
        username = msg['from']['username']
    except:
        firstname = msg['from']['first_name']
    user_id = msg['from']['id']
    
    if content_type == 'text':
        text = msg['text']
    
    if text == '/start':
        bot.sendMessage(chat_id, str("Come posso aiutarti?"), reply_markup=start_markup)
    elif text == 'Aiuto':
        bot.sendMessage(chat_id,'Bot sviluppato da Alessio')
    else:
        bot.sendMessage(chat_id,text)
"""

"""
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    service = get_service()
    spreadsheet_id = os.environ["GOOGLE_SPREADSHEET_ID"]
    range_name = os.environ["GOOGLE_CELL_RANGE"]

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return render_template('index.html', values=values)


if __name__ == '__main__':
    app.run(debug=True)
"""

TOKEN = os.environ["BOT_TOKEN"]
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ....')
# Keep the program running.
while 1:
    time.sleep(10)
