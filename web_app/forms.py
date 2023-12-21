from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, DateField, TextAreaField, SelectMultipleField, RadioField


class EserForm(FlaskForm):
    eser_id = IntegerField(label="ID", validators=[DataRequired()])
    eser_adi = StringField(label="Ad", validators=[DataRequired()])
    eser_yazari = StringField(label="Sanatçı", validators=[DataRequired()])
    eser_tarihi = DateField(label="Tarihi", validators=[DataRequired()])
    eser_aciklama = TextAreaField(label="Açıklama", validators=[DataRequired()])


class SergiForm(FlaskForm):
    sergi_id = IntegerField(label="ID", validators=[DataRequired()])
    sergi_adi = StringField(label="Adı", validators=[DataRequired()])
    sergi_tarihi = DateField(label="Tarihi", validators=[DataRequired()])
    sergi_tipi = RadioField(label="Sergideki Eserler", choices=[("Daimi"), ("Tematik"), ("Geçici"), ],
                                    validators=[DataRequired()])
    sergi_aciklama = TextAreaField(label="Açıklama", validators=[DataRequired()])
    sergideki_eserler = SelectMultipleField(label="Sergideki Eserler", validators=[DataRequired()], coerce=int)
