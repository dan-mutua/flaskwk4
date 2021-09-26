from flask import Flask,render_template
import requests
import json




def pickquote():
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = req.content
    return data