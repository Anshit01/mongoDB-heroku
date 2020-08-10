from flask import Flask, render_template, request
from pymongo import MongoClient
from flask_cors import CORS
import requests
from app.config import username, password

app = Flask(__name__)
CORS(app)

cluster = MongoClient(f'mongodb+srv://{username}:{password}@mongodb-heroku-db-uw5of.mongodb.net/test?retryWrites=true&w=majority')
collection = cluster['test-db']['test-collection']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_all')
def load_all():
    results = collection.find({})
    ids = []
    names = []
    for result in results:
        ids.append(result['_id'])
        names.append(result['name'])
    l = len(ids)
    return render_template('table.html', len=l, ids=ids, names=names)

@app.route('/request')
def request_demo():
    response = requests.get("https://clock-anshit.herokuapp.com/")
    return response.text

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if(request.method == 'GET'):
        return render_template('insert.html', response=0)
    else:
        data = dict(request.form)
        if(data['_id'] == '' or data['name'] == ''):
            return render_template('insert.html', response=2, error_msg='Enter some data first!')
        try:
            collection.insert_one(data)
            return render_template('insert.html', response=1)
        except Exception as e:
            return render_template('insert.html', response=2, error_msg=str(e))
