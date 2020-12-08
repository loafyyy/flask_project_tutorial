from wtforms import Form, IntegerField, validators
from wtforms.validators import DataRequired

class MathForm(Form):
    int_input = IntegerField('Integer input', validators=[validators.NumberRange(min=-100, max=100)])
