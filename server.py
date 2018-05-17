import json
import os
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/data1', methods=['POST'])
def data1():
    data = [["date", "power_consumption", {'role': 'style'}]]
    with open(os.path.join('/home/jaeshin/htmlserver/data', request.form['m'],
                           'output{}.txt'.format(request.form['m']))) as fp:
        lines = fp.readlines()

        n = 0
        temp = 0
        for line in lines:
            line = line.strip()
            mon, day, _, power = line.split()
            temp += float(power)
            if((n+1) % 24 == 0):
                data.append(["{}월{}일".format(mon, day, int(n/24)), float(temp), "#FF0000"])
                temp = 0;
            n += 1

    resp = make_response(json.dumps({'data': data}))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/data2', methods=['POST'])
def data2():
    data = [["date", "power_consumption", {'role': 'style'}]]
    with open(os.path.join('/home/jaeshin/htmlserver/data', request.form['m'],
                           'output{}월{}일.txt'.format(request.form['m'], request.form['d']))) as fp:
        lines = fp.readlines()

        n = 0
        temp = 0
        for line in lines:
            line = line.strip()
            mon, day, _, power = line.split()
            temp += float(power)
            if((n+1) % 4 == 0):
                data.append(["{}월{}일{}시".format(mon, day, int(n/4)), float(temp), "#FF0000"])
                temp = 0
            n += 1

    resp = make_response(json.dumps({'data': data}))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run()
