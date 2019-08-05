from app import app
import os
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from config import Config

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    service = get_service()
    spreadsheet_id = os.environ["GOOGLE_SPREADSHEET_ID"]
    range_name = os.environ["GOOGLE_CELL_RANGE"]

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    """
    result = Config.SERVICE.spreadsheets().values().get(
        spreadsheetId=Config.SHEET, range=Config.RANGE_SITUAZIONE).execute()
    values = result.get('values', [])

    return render_template('index.html', values=values)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
