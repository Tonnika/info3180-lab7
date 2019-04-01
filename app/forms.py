from flask_wtf import Form 
from wtforms import TextAreaField, FileField 
from wtforms.validators import Length, InputRequired

class UploadForm(Form):
    description = TextAreaField('Description', Length(max=80),validators=[InputRequired()])
    photo = FileField('Photo') 
