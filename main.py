from flask import Flask, request, jsonify
from flask_cors import CORS
import unittest 

app = Flask(__name__)
CORS(app)

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/applications', methods=['POST'])
def applications():
    json = request.json
    requested_amount = int(json.get('requested_amount'))
    business_name = json.get('business_name')
    tax_id = int(json.get('tax_id'))
    limit_amount = 50000
    state = 'Undefined'
    if requested_amount > limit_amount: 
        state= 'Declined'
    elif requested_amount == limit_amount: 
        state= 'Undecided'
    elif requested_amount < limit_amount: 
        state= 'Approved'
    return jsonify({
        'state': state,
        'requested_amount': requested_amount,
        'business_name': business_name,
        'tax_id': tax_id,
    })
