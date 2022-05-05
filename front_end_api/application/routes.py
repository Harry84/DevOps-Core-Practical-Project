from . import app 
from flask import Flask, request, Response, redirect, render_template
import requests, json


@app.route('/', methods=['POST', 'GET'])
def index(): 
    pilot = requests.get('http://pilot_api:5000/get_pilot').text
    tier = requests.get('http://tier_api:5000/get_tier').text

    content = {'pilot': pilot, 'tier': tier}
    status = requests.post('http://service_4:5000/post/status', json=content).json()

    statement = f"You generated a {status['pilot']} pilot, {status['tier']}: {status['message']}"

    return render_template('index.html', statement=statement)
    # return Response(f"{status['pilot']} {status['tier']} {status['message']}")