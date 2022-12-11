import os
from flask import Flask, jsonify, send_from_directory
from src.controller.index import Index
from src.controller.jsonapi import JsonApi

app = Flask(__name__)

@app.route("/")
def index():
    idx = Index()
    return idx.index()

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'image/favicon.ico', 
        mimetype='image/vnd.microsoft.icon'
    )

@app.route("/jsonapi")
def jsonapi():
    ja = JsonApi()
    return jsonify(ja.index())