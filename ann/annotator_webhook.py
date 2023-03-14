# annotator_webhook.py
#
# NOTE: This file lives on the AnnTools instance
# Modified to run as a web server that can be called by SNS to process jobs
# Run using: python annotator_webhook.py
#
# Copyright (C) 2015-2023 Vas Vasiliadis
# University of Chicago
##
__author__ = "Vas Vasiliadis <vas@uchicago.edu>"

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.url_map.strict_slashes = False

# Get configuration and add to Flask app object
environment = "annotator_webhook_config.Config"
app.config.from_object(environment)

# Connect to SQS and get the message queue

@app.route("/", methods=["GET"])
def annotator_webhook():

    return ("Annotator webhook; POST job to /process-job-request"), 200

"""
A13 - Replace polling with webhook in annotator

Receives request from SNS; queries job queue and processes message.
Reads request messages from SQS and runs AnnTools as a subprocess.
Updates the annotations database with the status of the request.
"""

@app.route("/process-job-request", methods=["GET", "POST"])
def annotate():

    print(request)

    if request.method == "GET":

        return jsonify({"code": 405, "error": "Expecting SNS POST request."}), 405

    elif request.method == "POST":

        # Check message type

        # Confirm SNS topic subscription

        # Process job request

        return (
            jsonify({"code": 200, "message": "Annotation job request processed."}),
            200,
        )

### EOF