from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Juanda deje la paja'

@app.route('/name/<value>')
def name(value):
    val = {"value":value}
    return jsonify(val)

@app.route('/mail/<value>')
def mail(value):
    val = {"value":value}
    return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)