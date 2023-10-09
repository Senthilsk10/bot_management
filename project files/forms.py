from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, FileField, SelectField, SubmitField, HiddenField
from wtforms.validators import DataRequired


available_categories = [
    ("Music", "Music"),
    ("Video", "Video"),
    ("Games", "Games"),
    ("Movies", "Movies"),
    ("Productivity", "Productivity"),
    ("Social", "Social"),
    ("Health & Fitness", "Health & Fitness"),
    ("Education", "Education"),
    ("Technology", "Technology"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Food & Recipes", "Food & Recipes"),
    ("News", "News"),
    ("Weather", "Weather"),
    ("Sports", "Sports"),
    ("Art & Design", "Art & Design"),
    ("Finance", "Finance"),
    ("Home & Lifestyle", "Home & Lifestyle"),
    ("Other", "Other"),  # You can include other category or change the existed one
]


class AddBotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    details = TextAreaField('Details')
    links = StringField('Links', validators=[DataRequired()])
    youtube_demo_link = StringField('Youtube Demo Link')
    active = BooleanField('Active')
    photo = FileField('Photo')
    screenshot1_url = FileField('screenshot1_url')
    screenshot2_url = FileField('screenshot2_url')
    screenshot3_url = FileField('screenshot3_url')
    screenshot4_url = FileField('screenshot4_url')
    screenshot5_url = FileField('screenshot5_url')
    category = SelectField('Category', choices=available_categories, validators=[DataRequired()])
    tags = StringField('Tags')
    submit = SubmitField('Add Bot')


class EditBotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    details = TextAreaField('Details', validators=[DataRequired()])
    links = StringField('Links', validators=[DataRequired()])
    youtube_demo_link = StringField('Youtube Demo Link', validators=[DataRequired()])
    active = BooleanField('Active')
    photo = FileField('Photo')
    screenshot1_url = FileField('screenshot1_url')
    screenshot2_url = FileField('screenshot2_url')
    screenshot3_url = FileField('screenshot3_url')
    screenshot4_url = FileField('screenshot4_url')
    screenshot5_url = FileField('screenshot5_url')
    category = SelectField('Category', choices=available_categories)
    tags = StringField('Tags', validators=[DataRequired()])
    submit = SubmitField('Save Changes')


class FeedbackForm(FlaskForm):
    bot_name = HiddenField('Bot Name', validators=[DataRequired()])
    user_name = StringField('User Name', validators=[DataRequired()])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit Feedback')