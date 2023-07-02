from wtforms import Form, StringField, RadioField, TextAreaField, validators
from wtforms.fields import EmailField, DateField, IntegerField, PasswordField
import datetime



class CreateUserForm(Form):
    first_name = StringField('First Name*', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name*', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = RadioField('Gender*', [validators.DataRequired()], choices=[('F', 'Female'), ('M', 'Male')], default='')
    date_of_birth = DateField('Date of Birth*', [validators.DataRequired()])
    date_joined = DateField('Date Joined*', [validators.data_required()])
    email = EmailField('Email Address*', [validators.DataRequired()])
    phone = IntegerField('Phone Number*', [validators.data_required(),validators.NumberRange(min=10000000, max=99999999)])
    address = StringField('Address*', [validators.data_required()])
    password = PasswordField('Password*', [
        validators.EqualTo('c_password', message='Passwords must match', ),
        validators.data_required()
    ])
    c_password = PasswordField('Confirm Password*', [validators.data_required()])


    remarks = TextAreaField('Remarks', [validators.Optional()])


class LoginUserForm(Form):
    email = EmailField('Email Address', [validators.DataRequired()])
    phone = IntegerField('Phone Number',
                         [validators.data_required(), validators.NumberRange(min=10000000, max=99999999)])
    #make custom validator to ensure at least 1 of the 2 fields are filled in
    password = PasswordField('Password')


class LoginAdminForm(Form):
    email = EmailField('Email Address', [validators.DataRequired()])
    phone = IntegerField('Phone Number',
                         [validators.data_required(), validators.NumberRange(min=10000000, max=99999999)])
    #make custom validator to ensure at least 1 of the 2 fields are filled in
    password = StringField('Password')

    
    
class CreateCustomerOrderForm(Form):
    user_name = StringField('User Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
    name_of_item = StringField('Product ID:', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = IntegerField("Price (S$):", [validators.NumberRange(min=1, max=1000),validators.DataRequired()])
    no_of_items = IntegerField('no of items:', [validators.NumberRange(min=1, max=1000),validators.DataRequired()])
    email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
    collection = RadioField('do you wish to pick up the product(s) yourself?:',choices=['yes', 'no'])
    address = TextAreaField('If you prefer delivery, please enter your mailing address (type nil if you chose self pick up):', [validators.length(max=200),
                                                                                                                                validators.DataRequired()])
    total_price = IntegerField('total price(S$)(10% off for self pick-up):',[validators.NumberRange(min=1, max=1000),validators.DataRequired()])
    
class CreateUserOrderForm(Form):
    name_of_item = StringField('Product ID:', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = IntegerField("Price (S$):", [validators.NumberRange(min=1, max=1000),validators.DataRequired()])
    no_of_items = IntegerField('no of items:', [validators.NumberRange(min=1, max=1000),validators.DataRequired()])
    collection = RadioField('do you wish to pick up the product(s) yourself?:',choices=['yes', 'no'])
    address = TextAreaField('If you prefer delivery, please enter your mailing address (type nil if you chose self pick up):', [validators.length(max=200),
                                                                                                                                validators.DataRequired()])
    total_price = IntegerField('total price(S$)(10% off for self pick-up):',[validators.NumberRange(min=1, max=1000),validators.DataRequired()])

