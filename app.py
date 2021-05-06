from Flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, from Caleb!"

@app.route('/cowsay/<message>/')
def cowsay(message):
    # Code goes here.
    return "not yet"
