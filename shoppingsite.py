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

@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/shrimp")
def list_shrimp():
    """Return page showing all shrimp for sale"""
    shrimp_list = shrimp.get_all()
    return render_template("all_shrimp.html",
                           shrimp_list=shrimp_list)

@app.route("/shrimp/<shrimp_id>")
def show_shrimp(shrimp_id):
    """Return page showing the details of a given shrimp.

    Show all info about a shrimp. Also, provide a button to buy that shrimp.
    """

    shrimp = shrimp.get_by_id(shrimp_id)
    print(shrimp)
    return render_template("shrimp_details.html",
                           display_shrimp=shrimp)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")