
from flask import Flask,render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    print(req.content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)