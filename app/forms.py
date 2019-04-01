from flask_wtf import Form 
from wtforms import TextArea, FileField 
from wtforms.validators import Length

class UploadForm(Form):
    description = TextArea('Description', Length(max=80))
    photo = FileField('Photo') 
