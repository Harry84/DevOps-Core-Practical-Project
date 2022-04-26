from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_tier',methods=['GET'])
def name(): 
    tier_choice = ["S Tier", "A Tier", "B Tier", "C Tier", "Just Bad", "Uninstall Now"]
    tier_name = random.choice(tier_choice)
    return Response(f"{tier_name}", mimetype="text/plain")