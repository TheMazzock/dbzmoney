from app import app

"""
import os
from flask import Flask, render_template
import googleapiclient.discovery
from google.oauth2 import service_account
'''
import telepot, time, sqlite3, random, csv
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint

startkeyboard = [['Situazione', 'Inserimento', 'Conti']]
startmarkup = ReplyKeyboardMarkup(keyboard=startkeyboard, one_time_keyboard=False)

gruppialessio = ['PERSONALI ALESSIO','ENTRATE ALESSIO','SPESE ALESSIO','SALDO ALESSIO']
situazionekeyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Spese previste', callback_data='spesepreviste'),
                     InlineKeyboardButton(text='Ritorna', callback_data='ritorna')],
                 ])

gruppi = ['CONTI CORRENTI','CARTE','CONTANTI','ALTRO']
gruppiconti = ['ENTRATE','RATE FISSE','SPESE DI CASA','ANIMALI','MEZZI DI TRASPORTO','SPESE RICARDO','SPESE MEDICHE','DIVERTIMENTI','VARIE','EXTRA','TRANSITORI','PERSONALI ALESSIO','ENTRATE ALESSIO','SPESE ALESSIO','SALDO ALESSIO']
conti_range = "conti!A21:A130"
conti_result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=conti_range).execute()
conti_values = conti_result.get('values', [])
conti_lista = []
for x in conti_values:
    if x[0] in gruppiconti:
        pass
    else:
        conti_lista.append([x[0]])
contimarkup = ReplyKeyboardMarkup(keyboard=conti_lista, one_time_keyboard=False)

     
def situazione(cid):
    output=""
    range_name = "database!D1:D10"
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    print(values)
    keyboard=[]
    range_situazione = "situazione!A2:E14"
    rsituazione = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_situazione).execute()
    dbsituazione = rsituazione.get('values', [])
    for x in dbsituazione:
        if x[0] in gruppi:
            print(x[0])
            output = output + x[0]+"\n"
        else:
            print(x)
            output = output + x[0] + "\t" + x[1] + "\n"
    bot.sendMessage(cid, output)
    bot.sendMessage(cid, 'Seleziona', reply_markup=startmarkup)

  
      
'''
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

