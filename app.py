from assign1 import *
from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS, cross_origin
import requests
import json
import time


app = Flask(__name__, static_url_path='/static')


CORS(app, resources={r"/*":{"origin":"*", }})
app.config["CORS_Credentials"]=True
app.config["CORS_HEADER"] = "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale,X-Requested-With"
app.config["CORS_Methods"]="POST, OPTIONS, GET, DELETE, HEAD"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image/quantizer', methods= ['GET', 'POST'])
def image_quantizer():
    if request.method == 'POST':
        file = request.files['file']
        quantize = int(request.form.get('quantize'))
    # if(file == "" or quantize%0 != 0 or quantize == ""):
    #     return render_template('index.html')
    value = quantizer(file,quantize)
    time.sleep(7)
    return render_template('results.html', values=value)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)