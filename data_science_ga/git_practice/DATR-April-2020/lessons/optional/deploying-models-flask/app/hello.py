import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return '''
    <body>
    <h2> Hello World! <h2>
    </body>
    '''

@app.route("/greet/<name>")
def greet(name):
    """docstring here"""
    return "Hello, {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)