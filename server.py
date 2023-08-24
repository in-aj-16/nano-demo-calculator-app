from flask import Flask, request, jsonify
app = Flask(_name_)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    n1 = data['first']
    n2 = data['second']
    return jsonify({'result': n1 + n2}), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    n1 = data['first']
    n2 = data['second']
    return jsonify({'result': n1 - n2}), 200

if _name_ == '_main_':
    app.run(port=8081,host='0.0.0.0')