import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


username = 'root'
password = '102531'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost/PUPPY_ADOPTION'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False