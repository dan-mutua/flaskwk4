
from flask import Flask
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    return 'taraa'

if __name__ == '__main__':
    app.run(debug = True)