import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import googleapiclient.discovery
from google.oauth2 import service_account

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
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
