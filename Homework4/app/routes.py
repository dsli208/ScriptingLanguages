from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import CalculatorForm

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

# error
@app.route('/')
@app.route('/result/error', methods=['GET', 'POST'])
def error():
    return "Error.  Please try again."

# add
@app.route('/')
@app.route('/result/add', methods=['GET', 'POST'])
def add(num1, num2):
    sum = num1 + num2
    resultStr = "The result is " + sum
    return resultStr

# multiply
@app.route('/')
@app.route('/result/multiply', methods=['GET', 'POST'])
def multiply(num1, num2):
    product = num1 * num2
    resultStr = "The result is " + product
    return resultStr

# subtract
@app.route('/')
@app.route('/result/subtract', methods=['GET', 'POST'])
def subtract(num1, num2):
    diff = num1 + num2
    resultStr = "The result is " + diff
    return resultStr

# divide
@app.route('/')
@app.route('/result/divide', methods=['GET', 'POST'])
def divide(num1, num2):
    quotient = num1 + num2
    resultStr = "The result is " + quotient
    return resultStr

# for the calculator form
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    num1 = 0
    num2 = 0
    try:
        num1 = float(form.num1)
        num2 = float(form.num2)
    except ValueError:
        return redirect(url_for('error'))
    if form.mode == "Add":
        return redirect(url_for('add'))
    elif form.mode == "Subtract":
        return redirect(url_for('subtract'))
    elif form.mode == "Multiply":
        return redirect(url_for('multiply'))
    elif form.mode == "Divide":
        return redirect(url_for('divide'))
    else:
        return redirect(url_for('error'))
