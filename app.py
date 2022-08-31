import os

from flask import Flask, render_template, request, url_for, redirect, flash, session
from werkzeug.utils import secure_filename

from models import db, LoanModel, AdminModel, ProductModel, ClientModel, InvestmentModel
from datetime import date, datetime

app = Flask(__name__)

app.secret_key = "secret-key"
UPLOAD_FOLDER = 'static/files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods={'GET','POST'})
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            return redirect('/')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/loan_list')
def loan_list():
    return render_template('loan_list.html')


if __name__ == '__main__':
    app.run(debug=True)
