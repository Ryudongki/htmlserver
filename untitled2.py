import json
import os
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('a.html')

@app.route('/data', methods=['POST'])
def data():
    data = [["date", "power_consumption", {'role': 'style'}]]
    with open(os.path.join('C:/Users/user/PycharmProjects/untitled2\data', request.form['m'], 'output{}월{}일.txt'.format(request.form['m'], request.form['d']))) as fp:
        lines = fp.readlines()

        n = 0
        for line in lines:
            n += 1
            line = line.strip()
            mon, day, _, power = line.split()
            data.append(["{}월{}일{}분기".format(mon, day, n), float(power), "#FF0000"])

    resp = make_response(json.dumps({'data': data}))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run()
