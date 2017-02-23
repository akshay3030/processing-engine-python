from calculator import Calculator,DataInput
import sys
import importlib


from flask import Flask, request, jsonify
app = Flask(__name__)
#app.run(host='localhost', port=8075)
#app.config['SERVER_NAME']	=	'127.0.0.1:8075'
app.config['SERVER_NAME']	=	'localhost:8075'


def load_class(full_class_string):
    """
    dynamically load a class from a string
    """
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_str)

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

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
    app.run(debug = True)
