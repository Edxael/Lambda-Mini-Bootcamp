
#           Homework #2
# https://github.com/SunJieMing/python-minicamp-homework-2
# Special thanks to @Taic who help me to understand the last part of the extra credit.

# -------------------------------------

# from flask import Flask
from flask import Flask, render_template, jsonify
app = Flask(__name__)


# -------------------------------------

# 01-Setup your initial route at / to return 'Hello World'.
#   Example: A GET request to localhost:5000/ would return 'Hello World'.
@app.route("/")

    # Now we write a function that tells the Route what to do
def index():
    return "Hello Edxael"

# -------------------------------------

# Build a route called /birthday that returns your birthday as a string in this format: 'October 30 1911'.
#   Example: A GET request to localhost:5000/birthday returns 'October 30 1911' (Use your birthday instead)
@app.route("/birthday")
def birthday():
    return "July 01 1992"

# -------------------------------------

# Build a route called /greeting that accepts a parameter called name. The route should return a string that says 'Hello <name>' where <name> is the name that you passed to the route.
#   Example: A GET request to localhost:5000/greeting/ben would return 'Hello ben!'
@app.route("/greeting/<name>")
def greeting(name):
    return "Hello {}".format(name)

# -------------------------------------
# Modify your home route (/) to return the html template provided below.
# .
#   -Create a folder called templates in the root of your project's directory.
#   -Create a file called home.html in the templates directory.
#   -Paste the HTML shown below into home.html and save.
#   -In your main server file modify the flask import line to say: from flask import Flask, render_template
#   -In your home (/) route return render_template('home.html').
#   -Navigate to localhost:5000/ and you should see the rendered HTML.
@app.route("/template1")
def template1():
    return app.send_static_file("home.html")

# -------------------------------------
#                     Extra Credit
# .
# Create a route called /sum that adds two parameteres together and returns them.
# .
#   -localhost:5000/sum/5/10 would return '15'
#   -You will need to convert the parameters to integers using int()
#   -Example: fiveAsInt = int('5') => fiveAsInt == 5
#   -You then have to convert the int back into a string using str()
#   -Example: fiveAsString = str(5) => fiveAsString == '5'
#   -You can also prefix the parameter with the keyword int => <int:param>. Make sure you turn it back into a string

@app.route("/sum/<int:num1>/<int:num2>")
def sum(num1, num2):
    total = num1 + num2
    return "The SUM of: " + str(num1) + " and " + str(num2) + " is: " + str(total)

# -------------------------------------
# Create a route called /multiply and a route called /subtract
# .
#   -localhost:5000/multiply/6/5 would return '30'
#   -localhost:5000/subtract/25/5 would return '20'
#   -Make sure you are converting the parameters to ints and returning a string

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    total = num1 * num2
    return "The MULTIPLICATION of: " + str(num1) + " and " + str(num2) + " is: " + str(total)

        # -----------

@app.route("/subtract/<int:num1>/<int:num2>")
def subtract(num1, num2):
    total = num1 - num2
    return "The SUBSTRACTION of: " + str(num1) + " minus " + str(num2) + " is: " + str(total)

# -------------------------------------
# Create a route called /favoritefoods that returns a list of your favorite foods
# .
#   -A list is a collection of different values. => ['football', 'basketball', 'rugby']
#   -The server must return a string so we need to convert our list into a string.
#   -One common string format for sending complex data is JSON.
#   -Change the top line of your server file to from flask import Flask, render_template, jsonify
#   -Pass your list to jsonify() when returning it. return jsonify(myList)

@app.route("/favfood")
def favfood():
     listx= ["Pizza", "Hamburger", "HotDog"]
     return jsonify(listx)
