from flask import Flask,render_template
import requests
import json




def pickquote():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = json.loads(req.content)
    return data

def pickquote1():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = json.loads(req.content)
    return data

def pickquote2():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = json.loads(req.content)
    return data        