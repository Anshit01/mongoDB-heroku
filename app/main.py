from flask import Flask, render_template
#from pymongo import MongoClient
import requests

app = Flask(__name__)

#cluster = MongoClient('mongodb+srv://anshit01:uu66xdT!A4aQL-e@mongodb-heroku-db-uw5of.mongodb.net/test?retryWrites=true&w=majority')
#collection = cluster['test-db']['test-collection']

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/load_all')
# def load_all():
#     results = collection.find({})
#     s = ''
#     for result in results:
#         s += str(result) + '<br>'
#     return s

@app.route('/request')
def request():
    response = requests.get("https://clock-anshit.herokuapp.com/")
    return response.text
