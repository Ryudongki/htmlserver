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

    a = fp.readlines()
    dic = {}
    temp1, temp2, temp3 = [], [], []
    num1 = 0

    for k in a:
        temp = k.split(" ")
        temp = [float(t) for t in temp[:]]
        temp1.append(temp[0])
        temp2.append(temp[1])
        temp3.append(temp[3])
        dic['a' + str(num1)] = temp1[num1]
        dic['b' + str(num1)] = temp2[num1]
        dic['c' + str(num1)] = temp3[num1]
        num1 = num1 + 1

    resp = make_response(json.dumps(dic))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()
