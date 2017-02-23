import sys
import importlib


from flask import Flask, request, jsonify
app = Flask(__name__)
#app.run(host='localhost', port=8075)
#app.config['SERVER_NAME']	=	'127.0.0.1:8075'
#app.config['SERVER_NAME']	=	'localhost:8075'


def load_from_module(full_class_string):
    """
    dynamically load a class or function from a module using string
    """
    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_str)

@app.route("/hello/<name>")
def hello(name):
    return 'Hello from:%s' % name

#@app.route("/calculate/<model_name>", methods=['GET', 'POST'])
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    content = request.json
    model_name = request.args.get('model_name')
    
    # load_from_module function can load a Class as well as a function form a .py file, give the full path till class or method level
    #Calculator_class = load_from_module('model.Calculator.Calculator_cls')
    #Calculator_Obj  = Calculator_class()
    #Calculator_Obj.calculate(5,6)
    
    #Loading the function with name 'calculate' from <model_name.py> file at run time
    calculator  = load_from_module('model.'+model_name+'.calculate')
    return 'Calculated value:%s \n' % calculator(content['x'],content['y'])

if __name__ == "__main__":
    #app.run(debug = True)
    #app.run(debug = False,host='localhost', port=9090)
    
    #host='0.0.0.0' will make all income trafic work form other hosts outside of local host
    app.run(host='0.0.0.0')

