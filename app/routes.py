from app import app
from flask import render_template, flash, redirect, url_for,request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug import url_parse


@app.route('/')

@app.route('/index')
@login_required
def index():
    user = {'username': 'Dimitrius  '}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beatiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', posts = posts)


# This is everything that is required in my login route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # This initializes the login form from my forms.py file.
    form = LoginForm()
    # we are checking if the form is validating when you click submit. 
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        # This method is checking if the sign in works, if it doesnt it flashes a message and redirects them back to the login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
        return redirect(url_for('index')) # If my code doesnt work I should delete this line of code and the one under it
    return render_template('login.html', title = 'Sign In', form = form)
        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

