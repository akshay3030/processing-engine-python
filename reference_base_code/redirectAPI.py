from flask import Flask, abort, redirect, request # $ pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    if request.url.startswith('http://'):
        return redirect(request.url.replace('http', 'https', 1)
                        .replace('080', '443', 1))
    elif request.url.startswith('https://'):
        return 'Hello HTTPS World!'
    abort(500)

def https_app(**kwargs):
    import ssl
    context = ('./server.pem', './key.pem')
    app.run(ssl_context=context, **kwargs)


if __name__ == "__main__":
    from multiprocessing import Process

    kwargs = dict(host='localhost')
    Process(target=https_app, kwargs=dict(kwargs, port=443)).start()
    app.run(port=80, **kwargs)