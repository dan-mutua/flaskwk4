from flask import Flask,render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    req= requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    print(req.content)

    return render_template('quote.html')