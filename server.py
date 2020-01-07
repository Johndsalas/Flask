from flask import Flask
import random as r

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def page2():
    one = r.randint(1,10)
    two = r.randint(1,10)
    three = r.randint(1,10)
    return f"{one} {two} {three}"

