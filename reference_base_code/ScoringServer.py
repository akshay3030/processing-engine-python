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

#@app.route("/calculate/<model_name>", methods=['GET', 'POST'])
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    content = request.json
    model_name = request.args.get('model_name')
    # load_class function can load a Class as well as a function form a .py file, give the full path till class or method level
    calculator  = load_class('model.'+model_name+'.calculate')
    return 'Calculated value:%s \n' % calculator(content['x'],content['y'])

if __name__ == "__main__":
    app.run(debug = True)
