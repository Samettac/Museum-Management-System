from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import (StringField, IntegerField, DateField, TextAreaField, SelectMultipleField,
                     RadioField, PasswordField, SubmitField)


# Eser özelliklerini içeren form öğesi
class EserForm(FlaskForm):
    eser_id = IntegerField(label="ID", validators=[DataRequired(), NumberRange(min=1, message="id min 1 olabilir")])
    eser_adi = StringField(label="Ad", validators=[DataRequired()])
    eser_yazari = StringField(label="Sanatçı", validators=[DataRequired()])
    eser_tarihi = DateField(label="Tarihi", validators=[DataRequired()])
    eser_aciklama = TextAreaField(label="Açıklama", validators=[DataRequired()])
    submit = SubmitField(label="Gönder")


# Sergi özelliklerini içeren form öğesi
class SergiForm(FlaskForm):
    sergi_id = IntegerField(label="ID", validators=[DataRequired(), NumberRange(min=1, message="id min 1 olabilir")])
    sergi_adi = StringField(label="Adı", validators=[DataRequired()])
    sergi_tarihi = DateField(label="Tarihi", validators=[DataRequired()])
    sergi_tipi = RadioField(label="Sergideki Eserler", choices=[("Daimi"), ("Tematik"), ("Geçici"), ],
                                    validators=[DataRequired()])
    sergi_aciklama = TextAreaField(label="Açıklama", validators=[DataRequired()])
    sergideki_eserler = SelectMultipleField(label="Sergideki Eserler", validators=[DataRequired()], coerce=int)
    submit = SubmitField(label="Gönder")


# Etkinlik özelliklerini içeren form öğesi
class EtkinlikForm(FlaskForm):
    etkinlik_id = IntegerField(label="ID", validators=[DataRequired(), NumberRange(min=1, message="id min 1 olabilir")])
    etkinlik_adi = StringField(label="Ad", validators=[DataRequired()])
    etkinlik_tarihi = DateField(label="Tarihi", validators=[DataRequired()])
    etkinlik_aciklama = TextAreaField(label="Açıklama", validators=[DataRequired()])
    submit = SubmitField(label="Gönder")

