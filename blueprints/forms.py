from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    DecimalField,
    FloatField,
    HiddenField,
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TimeField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
    Optional,
    ValidationError
)
valid_license = {"district":["DHAKA", 
                       "NARAYANGANJ", 
                       "GAZIPUR",
                       "CHATTOGRAM",
                       "KHULNA",
                       "COMILLA",
                       "SYLHET",
                       "RAJSHAHI",
                       "RANGPUR",
                       "BARISAL",
                       "MYMENSINGH"],
            "class_code":[
                        "A",
                        "HA",
                        "LA",
                        "KA",
                        "KHA",
                        "GA",
                        "BHA",
                        "GHA",
                        "CHA",
                        "PA",
                        "CAA",
                        "JA",
                        "JHA",
                        "BA",
                        "SA",
                        "TWA",
                        "TAW",
                        "DWA",
                        "FA",
                        "THA",
                        "MA",
                        "NA",
                        "AU",
                        "DA",
                        "U",
                        "TA",
                        "DHA",
                        "SHA",
                        "E",
                        ]
}

def validate_car_license(form, field):
    try:
        district, class_code, block_1, block_2 = field.data.split("-")
    except ValueError:
        raise ValidationError('License number must be in format: DISTRICT-CLASS-XX-XXXX')
    
    # Validate district and class separately for more specific error messages
    if district not in valid_license.district:
        raise ValidationError(f'Invalid district code.')
    
    if class_code not in valid_license.classes:
        raise ValidationError(f'Invalid class code.')
    
    # Validate numeric blocks
    try:
        block_1_num = int(block_1)
        block_2_num = int(block_2)

        if not 11<=block_1_num<=99:
            raise ValidationError('Invalid registration series')
        if block_2_num>9999:
            raise ValidationError('Invalid vehicle number')
    except ValueError:
        raise ValidationError('Last two blocks must be valid numbers')
class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(message="Enter First Name")])
    last_name = StringField('Last Name', validators=[DataRequired(message="Enter Last Name")])
    address = StringField('Address', validators=[DataRequired(message="Enter Address")])
    phone = StringField('Phone', validators=[DataRequired(message="Enter Phone Number"), Length(min=11, max=11)])
    car_license = StringField('License number', validators=[DataRequired(message="Enter License Number"), validate_car_license])
    car_engine = StringField('Engine number', validators=[DataRequired(message="Enter Engine Number")] )
    submit = SubmitField('Submit')

        

        
        

