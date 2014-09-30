# coding: utf-8

import logging
import flask
import json
import flask_config

app = flask.Flask(__name__)

app.static_folder = "templates"
app.SEND_FILE_MAX_AGE_DEFAULT = 0


@app.route('/webhook', methods=['POST'])
def strip2mailchimp():
	"""
	{
	  "created": 1326853478,
	  "livemode": false,
	  "id": "evt_00000000000000",
	  "type": "charge.succeeded",
	  "object": "event",
	  "request": null,
	  "data": {
	    "object": {
	      "id": "ch_00000000000000",
	      "object": "charge",
	      "created": 1412117456,
	      "livemode": false,
	      "paid": true,
	      "amount": 100,
	      "currency": "eur",
	      "refunded": false,
	      "card": {
	        "id": "card_00000000000000",
	        "object": "card",
	        "last4": "4242",
	        "brand": "Visa",
	        "funding": "credit",
	        "exp_month": 8,
	        "exp_year": 2015,
	        "fingerprint": "3WqOgApKDjCTvHEG",
	        "country": "US",
	        "name": null,
	        "address_line1": null,
	        "address_line2": null,
	        "address_city": null,
	        "address_state": null,
	        "address_zip": null,
	        "address_country": null,
	        "cvc_check": "pass",
	        "address_line1_check": null,
	        "address_zip_check": null,
	        "customer": null
	      },
	      "captured": true,
	      "refunds": {
	        "object": "list",
	        "total_count": 0,
	        "has_more": false,
	        "url": "/v1/charges/ch_14iZSOLQaIfBBJAWXuK7DE0I/refunds",
	        "data": []
	      },
	      "balance_transaction": "txn_00000000000000",
	      "failure_message": null,
	      "failure_code": null,
	      "amount_refunded": 0,
	      "customer": null,
	      "invoice": null,
	      "description": "My First Test Charge (created for API docs)",
	      "dispute": null,
	      "metadata": {},
	      "statement_description": null,
	      "receipt_email": null,
	      "receipt_number": null
	    }
	  }
	}
	"""

	
	event_json = json.load(request.body)
	print event_json
	
	return {}


@app.route('/')
def home():
	"""Returns html with an overview of shapes to compare the sizes-of """


	return file('templates/index.html').read()


if __name__ == '__main__':
	# Set up logging to stdout, which ends up in Heroku logs
	stream_handler = logging.StreamHandler()
	stream_handler.setLevel(logging.WARNING)
	app.logger.addHandler(stream_handler)

	app.debug = False
	app.run(host='0.0.0.0', port=flask_config.port)
