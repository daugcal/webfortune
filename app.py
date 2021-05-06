from flask import *
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('fortune'))
@app.route('/fortune/')
def fortune():
    # strings "<pre>" and "</pre>".
    result = os.popen('fortune').read()
    return ("<pre>"+result+"</pre>")    
@app.route('/cowsay/<message>/')
def cowsay(message):
    # Code goes here.
    result = os.popen('cowsay '+message).read()
    return ("<pre>"+result+"</pre>")    
    return message
@app.route('/cowfortune/')
def cowfortune():
    # Code goes here.
    fortune = os.popen('fortune').read()
    result = os.popen('cowsay '+fortune).read()
    return ("<pre>"+result+"</pre>")    
    return message
