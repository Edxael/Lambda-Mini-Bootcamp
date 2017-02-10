from flask import Flask
app = Flask(__name__)

# -------------------------------------
    # setting responses to HTTP Requests AKA: Creating the page
        # Creating the route
@app.route("/")

    # Now we write a function that tells the Route what to do
def index():
    return "Hello Edxael"

# -------------------------------------

    # About page
@app.route("/about")
def about():
    return "this is my About Page"

# -------------------------------------

    # About page
@app.route("/contact")
def contact():
    return "<h1> Contacts Page <h1><p>paragraph of info</p> "

# -------------------------------------
