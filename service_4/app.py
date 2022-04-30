from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/post/status', methods=['POST'])
def post_status():
    pilot = request.json['pilot']
    tier = request.json['tier']

    if tier == "S Tier":
        message = "You a God"
    elif tier == "A Tier":
        message = "Parent with skills"
    elif tier == "B Tier":
        message = "Don't give up the day job"
    else:
        message = "What a bot!"

    status = {
        "pilot": pilot,
        "tier": tier,
        "message": message
    }

    return jsonify(status)

if __name__ == '__main__':
    app.run(host='0.0.0.0')