from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bot(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  details = db.Column(db.Text, nullable=False)
  links = db.Column(db.String(255), nullable=True)
  youtube_demo_link = db.Column(db.String(255), nullable=True) 
  active = db.Column(db.Boolean, default=False)
  photo_url = db.Column(db.String(255), nullable=True, default = "/static/logo/download.png")
  screenshot1_url = db.Column(db.String(255), nullable=True,default = '/static/logo/botscreenshot.webp')
  screenshot2_url = db.Column(db.String(255), nullable=True)
  screenshot3_url = db.Column(db.String(255), nullable=True)
  screenshot4_url = db.Column(db.String(255), nullable=True)
  screenshot5_url = db.Column(db.String(255), nullable=True)
  category = db.Column(db.String(150), nullable=False)
  tags = db.Column(db.String(255), nullable=False)


class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(200), nullable=False)
  message = db.Column(db.Text, nullable=False)
  ph_no = db.Column(db.Integer, nullable=False)
  read = db.Column(db.Boolean, default=False)

class feedback(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  bot_name = db.Column(db.String(100), nullable=False)
  user_name = db.Column(db.String(100), nullable=False)
  feedback = db.Column(db.Text, nullable=False)

