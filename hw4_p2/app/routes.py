from flask import render_template, flash, redirect, url_for, get_flashed_messages, request
from app import app
from app.forms import CalculatorForm
import sys

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# error
@app.route('/error', methods=['GET', 'POST'])
def error():
    return "Error.  Please try again."

# result
@app.route('/result',methods=['GET', 'POST'])
def result():
    n = 0
    #try:
        #n = float(request.args.get('result'))
    #except ValueError:
        #n = -1000
    resultStr = "The result is "
    return render_template('/result.html', title="Result", result=n)
# add
@app.route('/result/add', methods=['GET', 'POST'])
def add():
    x = float(request.args['x'])
    y = float(request.args['y'])
    resultStr = "The result is " + str(x + y)
    print(resultStr, file=sys.stderr)
    #return render_template('add.html', title="Add Result")
    return resultStr

# multiply
@app.route('/result/multiply', methods=['GET', 'POST'])
def multiply():
    #resultStr = "The result is "
    #return render_template('multiply.html', title="Multiply Result")
    x = float(request.args['x'])
    y = float(request.args['y'])
    resultStr = "The result is " + str(x * y)
    print(resultStr, file=sys.stderr)
    #return render_template('add.html', title="Add Result")
    return resultStr

# subtract
@app.route('/result/subtract', methods=['GET', 'POST'])
def subtract():
    #resultStr = "The result is "
    #return render_template('subtract.html', title="Subtract Result")
    x = float(request.args['num1'])
    y = float(request.args['num2'])
    resultStr = "The result is " + str(x - y)
    print(resultStr, file=sys.stderr)
    # return render_template('add.html', title="Add Result")
    return resultStr

# divide
@app.route('/divide', methods=['GET', 'POST'])
def divide():
    #resultStr = "The result is "
    #return render_template('divide.html', title="Divide Result")
    x = float(request.args['num1'])
    y = float(request.args['num2'])
    resultStr = "The result is " + str(x / y)
    print(resultStr, file=sys.stderr)
    # return render_template('add.html', title="Add Result")
    return resultStr

# for the calculator form
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CalculatorForm()
    num1 = 0
    num2 = 0
    result = 0
    if form.validate_on_submit():
        try:
            num1 = float(form.num1)
            num2 = float(form.num2)
        except ValueError:
            return redirect(url_for('error'))
        if form.mode.data == 'add':
            result = num1 + num2

            #form.result.data = num1 + '+' + num2 + '=' + result
            flash(num1 + '+' + num2 + '=' + result)
            #return str(get_flashed_messages())
            return redirect(url_for('result', n=result))
        elif form.mode.data == 'subtract':
            result = num1 - num2
            flash(num1 + '-' + num2 + '=' + result)
            #return str(get_flashed_messages())
            return redirect(url_for('result', n=result))
        elif form.mode.data == 'multiply':
            result = num1 * num2
            flash(num1 + '*' + num2 + '=' + result)
            #return str(get_flashed_messages())
            return redirect(url_for('result', n=result))
        elif form.mode.data == 'divide':
            result = num1 / num2
            flash(num1 + '/' + num2 + '=' + result)
            #return str(get_flashed_messages())
            return redirect(url_for('result', n=result))
        else:
            return redirect(url_for('error'))

    return render_template('/base.html',title = 'Web Calculator', form=form)
