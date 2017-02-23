from calculator import Calculator,DataInput

from flask import Flask, request, jsonify

from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)



@app.route("/hello/<name>")
def hello(name):    
    return 'Hello from:%s' % name


@app.route("/hello2", methods=['POST'])
def hello2():
	content = request.json
    	return 'Hello %s' % content['name']


@app.route('/calculate', methods=['GET', 'POST'])
def add_message():
    content = request.json
    data = DataInput(content['x'],content['y'])
    calculator = Calculator()
    
    return 'Calculated value:%s' % calculator.calculate(data)


if __name__ == "__main__":
    context = ('./server.pem', './key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=False)
    