from flask import Flask, request, Response 
import random

app = Flask(__name__)

tier_choice = ["S Tier", "A Tier", "B Tier", "C Tier", "Just Bad", "Uninstall Now"]

@app.route('/get_tier',methods=['GET'])
def name():  
    return random.choice(tier_choice)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')