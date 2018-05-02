import json
import os
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('a.html')

@app.route('/data', methods=['POST'])
def data():
    fp = open(os.path.join('C:/Users/user/PycharmProjects/untitled2\data', request.form['m'], 'output{}월{}일.txt'.format(request.form['m'], request.form['d'])))
    print(fp.readlines())
    data = fp.readlines()
    key = 1

    a = {'a': 'abcd'}

    resp = make_response(json.dumps(a))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()
