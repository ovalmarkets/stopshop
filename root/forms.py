from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import MultipleFileField, FileRequired
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from root.model import users



class loginform(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[Length(min=2), DataRequired()])
    
    login = SubmitField(label="login")

class blogform(FlaskForm):
    title = StringField(validators=[DataRequired()])
    blogpost = StringField(validators=[Length(min=20,max=100), DataRequired()])
    post = SubmitField(label="P O S T")
    

