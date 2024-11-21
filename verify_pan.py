from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_pan_data():
    with open('pan_data.json', 'r') as file:
        return json.load(file)

@app.route('/verify_pan', methods=['POST'])
def verify_pan():
    pan_data = load_pan_data()
    requested_data = request.get_json(force=True)
    requested_pan = requested_data.get("pan")
    requested_dob = requested_data.get("dob")

    match_found = False

    for record in pan_data:
        if record['data']['pan_number'] == requested_pan and record['data']['dob'] == requested_dob:
            match_found = True
            break

    return jsonify({"matchingflag": match_found})

if __name__ == '__main__':
    app.run(debug=True)