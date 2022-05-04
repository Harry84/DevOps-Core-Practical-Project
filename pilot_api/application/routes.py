from flask import Flask, request, Response 
from application import app
import random

@app.route('/get_pilot',methods=['GET'])
def name(): 
    pilot_choice = ["Bomber", "Interceptor", "Flex", "Twilek", "Sullustan"]
    pilot_name = random.choice(pilot_choice)
    return Response(f"{pilot_name}", mimetype="text/plain")