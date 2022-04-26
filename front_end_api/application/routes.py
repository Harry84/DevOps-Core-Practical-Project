from application import app 
from flask import Flask, request, Response
import requests


@app.route('/', methods=['GET'])
def home(): 
    pilot_api = requests.get('http://pilot_api:5000/get_pilot')
    tier_api = requests.get('http://tier_api:5000/get_tier')
    return Response(f"{pilot_api.text} {tier_api.text}", mimetype="text/plain")