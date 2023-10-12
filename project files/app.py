from flask import (Flask, render_template, request, redirect, url_for, session,flash,send_file)
from forms import AddBotForm, EditBotForm
from models import db, Bot, Contact,feedback
import os
from flask_session import Session
from functools import wraps
from sqlalchemy import or_

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = 'senthil3226w'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_gallery.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db.init_app(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'telegram bots project'


Session(app)

app.config['admin_credentials'] = {"admin": "sword"}

with app.app_context():
  db.create_all()

def save_uploaded_photo(file):
  filename = os.path.join('uploads', file.filename)
  file.save(os.path.join(app.root_path, 'static', filename))
  return url_for('static', filename=filename)

def delete_uploaded_photo(file_url):
  if file_url:
    filename = file_url.split("/")[-1]
    image_path = os.path.join(app.root_path, 'static', 'uploads', filename)
    if os.path.exists(image_path):
      os.remove(image_path)

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'username' not in session:
      return redirect(url_for('admin_login'))
    return f(*args, **kwargs)
  return decorated_function

@app.route("/admin_login", methods=['POST', 'GET'])
def admin_login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    credentials = app.config['admin_credentials']
    if username in credentials and credentials[username] == password:
      session['username'] = admin
      return redirect(url_for("admin"))
  return render_template("admin_login.html")

@app.route('/add_bot', methods=['GET', 'POST'])
def add_bot():
    form = AddBotForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        details = form.details.data
        links = form.links.data
        youtube_demo_link = form.youtube_demo_link.data
        active = form.active.data
        category = form.category.data
        tags = form.tags.data
        
        # Check if data is received for the photo field
        if form.photo.data:
            photo_url = save_uploaded_photo(form.photo.data)
        else :
            photo_url = "/static/logo/download.png"
          # Set it to None if no data is received
        
        new_bot = Bot(
            name=name,
            description=description,
            details=details,
            links=links,
            youtube_demo_link=youtube_demo_link,
            active=active,
            category=category,
            tags=tags,
            photo_url=photo_url
        )

        for i in range(1, 6):
            screenshot_field_name = f"screenshot{i}_url"
            screenshot_file = getattr(form, screenshot_field_name).data
            if screenshot_file:
                screenshot_url = save_uploaded_photo(screenshot_file)
                setattr(new_bot, f"screenshot{i}_url", screenshot_url)
        
        db.session.add(new_bot)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('add_bot.html', form=form)


@app.route('/edit_bot/<int:bot_id>', methods=['GET', 'POST'])
def edit_bot(bot_id):
  bot = Bot.query.get(bot_id)
  if bot is None:
    return "Bot not found", 404
  form = EditBotForm(obj=bot)
  if form.validate_on_submit():
    form.populate_obj(bot)
    if form.photo.data:
      if bot.photo_url:
        delete_uploaded_photo(bot.photo_url)
      photo_url = save_uploaded_photo(form.photo.data)
      bot.photo_url = photo_url
    new_category = form.category.data
    if bot.category != new_category:
      bot.category = new_category
    bot.tags = form.tags.data
    db.session.commit()
    return redirect(url_for('admin'))
  return render_template('edit_bot.html', form=form, bot=bot)

@app.route('/edit_screenshots/<int:bot_id>', methods=['GET', 'POST'])
def edit_screenshots(bot_id):
  bot = Bot.query.get(bot_id)
  if bot is None:
    return "Bot not found", 404
  if request.method == 'POST':
    screenshot_number = request.form.get('screenshot_number')
    screenshot_field_name = f"screenshot{screenshot_number}_url"
    if screenshot_number and screenshot_number.isdigit() and int(
        screenshot_number) in range(1, 6):
      screenshot_url = getattr(bot, screenshot_field_name)
      screenshot_file = request.files.get(
        f"screenshot{screenshot_number}_file")
      if screenshot_file:
        if screenshot_url:
          delete_uploaded_photo(screenshot_url)
        screenshot_url = save_uploaded_photo(screenshot_file)
        setattr(bot, screenshot_field_name, screenshot_url)
        db.session.commit()
        return redirect(url_for('edit_screenshots', bot_id=bot.id))
  return render_template('edit_screenshots.html', bot=bot)

@app.route('/delete_screenshot', methods=['POST', 'GET'])
def delete_screenshot():
  bot_id = request.args.get('bot_id')
  screenshot_number = request.args.get('screenshot_number')
  if bot_id is None or screenshot_number is None:
    return jsonify({'error': 'Missing bot_id or screenshot_number'}), 400
  bot = Bot.query.get(bot_id)
  if bot is None:
    return jsonify({'error': 'Bot not found'}), 404
  screenshot_field = f"screenshot{screenshot_number}_url"
  setattr(bot, screenshot_field, None)
  db.session.commit()
  return redirect(url_for('edit_screenshots', bot_id=bot_id))

@app.route('/admin')
@login_required
def admin():
  contacts = Contact.query.all()
  sort_by = request.args.get('sort_by', 'name')
  search_query = request.args.get('search_query', '')
  query = Bot.query
  if sort_by == 'name':
    query = query.order_by(Bot.name)
  elif sort_by == 'active':
    query = query.order_by(Bot.active)
  if search_query:
    query = query.filter(
      Bot.name.ilike(f'%{search_query}%')
      | Bot.description.ilike(f'%{search_query}%'))
  bots = query.all()
  total_bots = len(bots)
  total_active_bots = sum(1 for bot in bots if bot.active)

  feedbacks = feedback.query.all()
  
  
  
  return render_template(
    'admin.html',
    bots=bots,
    sort_by=sort_by,
    search_query=search_query,
    total_bots=total_bots,
    total_active_bots=total_active_bots,
    message=contacts,feedbacks=feedbacks
  )

@app.route('/delete_bot/<int:bot_id>', methods=['GET'])
def delete_bot(bot_id):
  bot = Bot.query.get(bot_id)
  if bot is None:
    return "Bot not found", 404
  if bot.photo_url:
    filename = bot.photo_url.split("/")[-1]
    image_path = os.path.join(app.root_path, 'static', 'uploads', filename)
    if os.path.exists(image_path):
      return send_file(image_path, as_attachment=True)
  db.session.delete(bot)
  db.session.commit()
  return redirect(url_for('admin'))

@app.route('/contact/', methods=['POST', 'GET'])
def contact_form():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    ph_no = request.form['ph_no']
    message_text = request.form['message']
    new_message = Contact(name=name,
                          email=email,
                          ph_no=ph_no,
                          message=message_text)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for("contact_form"))
  return render_template("contact.html")

@app.route('/delete_contact/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
  contact = Contact.query.get(contact_id)
  if contact:
    db.session.delete(contact)
    db.session.commit()
  return redirect(url_for('admin'))

@app.route('/mark_as_read/<int:contact_id>', methods=['POST'])
def mark_as_read(contact_id):
  contact = Contact.query.get(contact_id)
  if contact:
    contact.read = True
    db.session.commit()
  return redirect(url_for('admin'))

category_order = {
  "Entertainment": ["Music", "Video", "Games", "Movies"],
  "Productivity": ["Productivity", "Education", "Technology"],
  "Lifestyle": [
    "Health & Fitness", "Travel", "Shopping", "Food & Recipes",
    "Home & Lifestyle", "Art & Design"
  ],
  "News & Information": ["News", "Weather", "Sports", "Finance"],
}

@app.route('/')
def index():
  selected_category = request.args.get('category')
  main_categories = list(category_order.keys())
  subcategories = []
  if selected_category:
    if selected_category in category_order:
      subcategories = category_order[selected_category]
      filtered_bots = Bot.query.filter(
        Bot.category.in_(subcategories)).order_by(Bot.category).all()
    else:
      return "Invalid category", 400
  else:
    subcategories = set([bot.category for bot in Bot.query.all()])
    filtered_bots = Bot.query.order_by(Bot.category).all()
  subcategories = [
    subcategory for subcategory in subcategories
    if any(bot.category == subcategory for bot in filtered_bots)
  ]
  search_query = request.args.get('search')
  search_results = []
  query = Bot.query
  if search_query:
    query = query.filter(
      or_(Bot.name.ilike(f"%{search_query}%"),
          Bot.description.ilike(f"%{search_query}%")))
    search_results = query.all()
  return render_template('index.html',
                         bots=filtered_bots,
                         selected_category=selected_category,
                         main_categories=main_categories,
                         subcategories=subcategories,
                         search_results=search_results)

@app.route('/view_bot/<int:bot_id>')
def bot_details(bot_id):
  bot = Bot.query.get(bot_id)
  feedback_entries = feedback.query.filter_by(bot_name=bot_id).all()

  if bot is None:
    return "Bot not found", 404
  similar_bots = Bot.query.filter(Bot.category == bot.category, Bot.id
                                  != bot_id).all()
  return render_template('bot.html', bot=bot, similar_bots=similar_bots, feedback_entries = feedback_entries)

@app.route('/tagview')
def tag_view():
    tag = request.args.get('tag')
  
    all_bots = Bot.query.all()
    
    bots_with_tag = []
    
    # Loop through all bots and check their tags
    for bot in all_bots:
        # Split the tags into a list
        tags_list = bot.tags.split(',')
        
        
        if tag in tags_list:
            bots_with_tag.append(bot)
    
    return render_template('tag.html', tag=tag, bots_with_tag=bots_with_tag)

@app.route('/search')
def search():
    
    search_query = request.args.get('search')
    
    # Perform a search based on the search input
    if search_query:
        
        filtered_bots = Bot.query.filter(
            or_(Bot.name.ilike(f"%{search_query}%"), Bot.description.ilike(f"%{search_query}%"))
        ).all()
    else:
        # If no search query is provided, display all bots
        filtered_bots = Bot.query.all()

    return render_template('search_results.html', search_query=search_query, bots=filtered_bots)




@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        bot_id = request.form['bot_id']
        user_name = request.form['user_name']
        feedback_text = request.form['feedback']

        
        new_feedback = feedback(bot_name=bot_id, user_name=user_name, feedback=feedback_text)

        try:
            # Add the feedback to the database
            db.session.add(new_feedback)
            db.session.commit()
            return redirect(url_for('bot_details', bot_id = int(bot_id)))  
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"  #check for error and diplyas it as html page without our layout

    return render_template('feedback_form.html')  


@app.route('/delete_feedback/<int:feedback_id>', methods=['POST'])
@login_required
def delete_feedback(feedback_id):
    feedback_item = feedback.query.get(feedback_id)
    if feedback_item:
        db.session.delete(feedback_item)
        db.session.commit()
        flash('Feedback deleted successfully!', 'success')
    else:
        flash('Feedback not found.', 'danger')

    return redirect(url_for('admin'))


@app.route('/about')
def hehe():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)