# app/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User, Post
from app.forms import LoginForm, SignupForm, PostForm
import markdown
from markupsafe import Markup

# Define Blueprint
main = Blueprint('main', __name__)

# Home route — shows all posts
@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    for post in posts:
        post.content_html = Markup(markdown.markdown(post.content))
    return render_template('index.html', posts=posts)

# Login route
@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("main.login"))
        login_user(user)
        return redirect(url_for("main.index"))
    return render_template("login.html", form=form)

# Signup route
@main.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for("main.login"))
    return render_template("signup.html", form=form)

# Logout route
@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))

# Create post
@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('main.index'))
    return render_template('post_form.html', form=form, title='Create Post')

# Edit post
@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash("You can't edit this post.")
        return redirect(url_for('main.index'))

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('main.index'))

    return render_template('post_form.html', form=form, title='Edit Post')

# Delete post
@main.route('/delete/<int:post_id>', methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash("You can't delete this post.")
        return redirect(url_for('main.index'))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!')
    return redirect(url_for('main.index'))
