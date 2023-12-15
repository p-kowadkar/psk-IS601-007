from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, URL

# psk 12/13/2023
class anime_db_FetchForm(FlaskForm):
    page_number = IntegerField('Page Number', [validators.NumberRange(min=1)], default=1)
    page_size = IntegerField('Page Size', [validators.NumberRange(min=1, max=1000)], default=10) 
    submit = SubmitField("Fetch")

# psk 12/13/2023
class anime_db_Form(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=255)])
    alternative_titles = StringField('Alternative_Titles', [validators.Length(min=1, max=255)])
    ranking = StringField('Ranking', [validators.Length(max=50)])
    type = StringField('type', [validators.Length(max=50)])
    genres = StringField('genres', [validators.Length(max=50)])
    episodes = StringField('episodes', [validators.Length(max=20)])
    status = StringField('Status', [validators.Length(max=50)])
    anime_type = StringField('Anime_Type', [validators.Length(max=20)])
    submit = SubmitField("Save")

# psk 12/13/2023
class anime_db_SearchForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('Title', [validators.Length(min=1, max=255)])
    alternative_titles = StringField('Alternative_Titles', [validators.Length(min=1, max=255)])
    ranking = StringField('Ranking', [validators.Length(max=50)])
    genres = StringField('Genres', [validators.Length(max=50)])
    episodes = StringField('Episodes', [validators.Length(max=20)])
    status = StringField('Status', [validators.Length(max=50)])
    sort = StringField("Sort")
    anime_type = StringField('Anime_Type', [validators.Length(max=20)])
    submit = SubmitField("Filter ")
    
class adminanime_db_SearchForm(anime_db_SearchForm):
    username = StringField("Username")
    
class anime_db_AssocForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    username = StringField("Username")
    anime_db = StringField("anime_db_Name")
    submit = SubmitField("Filter")