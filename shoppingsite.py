from flask import Flask, render_template, redirect, flash
import jinja2

import shrimp

app = Flask(__name__)

# Needed to use Flask sessioning features
app.secret_key = 'noonewilleverguessthis'

# Makes it so jinja won't silently fail on us
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
