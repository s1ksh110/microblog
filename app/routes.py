# app/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from app.forms import LoginForm, SignupForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.forms import PostForm
from app.models import Post
import markdown  # 🆕 Import markdown library
from markupsafe import Markup  # 🆕 To mark rendered HTML safe for Jinja2

# Define Blueprint
main = Blueprint('main', __name__)

# @main.route("/")
# @main.route("/index")
# def index():
#     return render_template("base.html", title="Home")

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

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    # 🆕 Convert Markdown to HTML
    for post in posts:
        post.content_html = Markup(markdown.markdown(post.content))
    return render_template('index.html', posts=posts)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('index'))
    return render_template('post_form.html', form=form, title='Create Post')

@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You cannot edit this post.')
        return redirect(url_for('index'))
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated.')
        return redirect(url_for('index'))
    return render_template('post_form.html', form=form, title='Edit Post')

@main.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You cannot delete this post.')
        return redirect(url_for('index'))
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.')
    return redirect(url_for('index'))