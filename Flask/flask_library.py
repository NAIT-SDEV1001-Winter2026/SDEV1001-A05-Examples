# What is Flask
# A lightweight/micro webserver for development of webpages using Python along with other tools (HTML, javaScript)
#to run the website: flask --app flask_library run --reload

from flask import Flask #import the Flask class
from flask import jsonify# turns python dictionaries into JSON data

app = Flask(__name__)#Create a flask object. __name__ is where it is.

#Create our home page. A page is called a route in python
#@ defines a decorator. 
#A route is always followed by a function that returns what is to be displayed 
@app.route("/") #Create a new route. / is the home page
def home():#does not need to be called home
    return """
    <html>
        <head>
            <title>Books Library</title>
        </head>
        <body>
            <h1>Welcome to the books library!!!</h1>
        </body>
    </html>
    """

books = [
    {"title":"1984","author":"George Orwell"},
    {"title":"Grilled Cheese","author":"Shane Bell"}
]


#A route to display all the books in a list as JSON data
@app.route("/books")
def books_list():
    return jsonify(books)#turn the list of book dictionaries into JSON format














