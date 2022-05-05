from flask import Flask, request, Response 
import random

app = Flask(__name__)

pilot_choice = ["Bomber", "Interceptor", "Flex", "Twilek", "Sullustan"]

@app.route('/get_pilot',methods=['GET'])
def name(): 
    return random.choice(pilot_choice)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')