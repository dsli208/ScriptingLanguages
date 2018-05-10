from flask import request
from flask_wtf import FlaskForm
from sqlalchemy.testing.pickleable import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, FloatField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class CalculatorForm(FlaskForm):
    num1 = FloatField('Number 1', validators=[DataRequired()])
    num2 = FloatField('Number2', validators=[DataRequired()])
    mode = RadioField('Mode', choices=[('add','Add (+)'),('subtract','Subtract (-)'), ('multiply', 'Multiply (*)'), ('divide', 'Divide (/)')])
    #try:
        #number1 = request.args.get('num1')
        #number2 = request.args.get('num2')
    #except ValueError:
        #number1 = 0
        #number2 = 0
        #result = StringField('Result')
    #mode_selection = request.args.get('mode')
    #if mode_selection == 'add':
        #result = StringField('Result', default=number1 + '+' + number2 + '=' + number1 + number2)
    #elif mode_selection == 'subtract':
        #result = StringField('Result', default=number1 + '-' + number2 + '=' + number1 - number2)
    #elif mode_selection == 'multiply':
        #result = StringField('Result', default=number1 + '-' + number2 + '=' + number1 * number2)
    #elif mode_selection == 'divide':
        #result = StringField('Result', default=number1 + '-' + number2 + '=' + number1 / number2)
    #else:
    #result = StringField('Result', default="Welcome to the Web Calculator")
    submit = SubmitField('Submit')