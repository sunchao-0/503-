from flask import Flask, render_template, request, jsonify
import time, os, requests, platform, json
from config.config import port
from sqlitedb.sqlitedb import sqlClass
from threading import Thread

app = Flask(__name__)
app.secret_key = '1996-05-16'
sql = sqlClass()
from route.login import cklogin

url = []


@app.route('/', methods=['GET', 'POST'])
@cklogin()
def index():
    if request.method == 'GET':
        return render_template('index.html', url=url)
    else:
        return jsonify(url)


if __name__ == '__main__':
    from route import *
    app.run(host='0.0.0.0',port=port,debug = False)
