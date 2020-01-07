from flask import Flask, render_template
import random as r
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/roll-dice/<int:ndice>')
def htmlpage(ndice):
    import random as r
    rolls = [r.randint(1, 6) for _ in range(ndice)]
    return render_template('dice.html', rolls=rolls)

@app.route('/my-first-form')
def my_first_form():
    return render_template('greetings.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greetings-result.html', greeting=greeting)

@app.route('/spam-filter')
def spam_input():
    return render_template('spam-filter.html')

@app.route('/spam-result', methods=['POST'])
def spam_output():
    import model as m
    msg = request.form['message']

    result = m.predict(msg)

    return render_template('spam-result.html',msg=msg,result=result)