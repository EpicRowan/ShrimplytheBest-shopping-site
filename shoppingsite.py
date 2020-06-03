from flask import Flask, render_template, redirect, flash, session
import jinja2

import shrimp

from flask_debugtoolbar import DebugToolbarExtension

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

    shrimps = shrimp.get_by_id(shrimp_id)
    print(shrimps)
    return render_template("shrimp_details.html",
                           display_shrimp=shrimps)

@app.route("/cart")
def show_shopping_cart():
	"""Display content of shopping cart."""

	order_total = 0

	cart_shrimp = []

	cart = session.get("cart", {})


	for shrimp_id, quantity in cart.items():

		shrimps = shrimp.get_by_id(shrimp_id)
		cost = shrimps.price
		

		total_cost = quantity * shrimps.price
		order_total += total_cost

		shrimps.quantity = quantity
		shrimp.total_cost = total_cost

		cart_shrimp.append(shrimps)


	print(cart)
	return render_template("cart.html",
							cart=cart_shrimp,
							order_total=order_total)

@app.route("/add_to_cart/<shrimp_id>")
def add_to_cart(shrimp_id):
    """Add shrimp to cart and redirect to shopping cart page.

    When a shrimp is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to
    cart'."""

    # Check if we have a cart in the session and if not, add one
    # Also, bind the cart to the name 'cart' for easy reference below
    if 'cart' in session:
        cart = session['cart']
    else:
        cart = session['cart'] = {}

    # We could also do this with setdefault:
    # cart = session.setdefault("cart", {})

    cart[shrimp_id] = cart.get(shrimp_id, 0) + 1

    # Print cart to the terminal for testing purposes
    print("cart:")
    print(cart)

    # Show user success message on next page load
    flash("Successfully added to cart.")

    # Redirect to shopping cart page
    return redirect("/cart")

@app.route("/register", methods = ["GET"])
def registration_form():

	return render_template("register_form.html")

@app.route("/register", methods = ["POST"])
def register():

	email = request.form["email"]
	password = request.form["password"]

	new_user = User(username = username, password = password)

	db.session.add(new_user)
	db.session.commit(new_user)
	return redirect("/")

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")

 
@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = user.get_by_email(email)

    if not user:
        flash("No such user", 'error')
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password", 'error')
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect(f"/users/{user.user_id}")


@app.route("/checkout")
def checkout():
  
    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/shrimp")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")