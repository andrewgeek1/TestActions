from flask import Flask, jsonify

app = Flask(name)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, Flask!"})

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({"result": a + b})

if name == 'main':
    app.run(debug=True)