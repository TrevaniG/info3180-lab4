from flask_wtf import FlaskForm
#from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired

#allowed = set('images',IMAGES)

class UploadForm(FlaskForm):
    upload=FileField('image',validators=[FileRequired(),FileAllowed(["png","jpg"],'Image files only!')])