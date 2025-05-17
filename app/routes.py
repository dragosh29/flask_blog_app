from flask import Blueprint, render_template

from app import db
from app.models import User, Post

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/user/profile/<int:user_id>')
def display_user_profile(user_id):
    user = User.query.get(user_id)
    return render_template('user.html', user=user)


@main.route('/users')
def display_all_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@main.route('/posts')
def display_all_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@main.route('/post/<int:post_id>')
def display_post(post_id):
    found_post = Post.query.get(post_id)
    if found_post:
        found_post.reads += 1
        db.session.commit()
    return render_template('post.html', post=found_post)
