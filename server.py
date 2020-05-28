from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Date, Meal, connect_to_db, db


app = Flask(__name__)

app.secret_key = "supersecret"

app.jinja_env.undefined = StrictUndefined