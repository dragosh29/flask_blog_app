from datetime import datetime
from app import create_app
from app.extensions import db
from app.models import User, Post, Comment

app = create_app()

with app.app_context():
    db.create_all()

    # Users to insert
    users_data = [
        {"username": "admin", "email": "admin@example.com", "age": 42},
        {"username": "user", "email": "user@example.com", "age": 20},
        {"username": "john_doe", "email": "john.doe@example.com", "age": 30},
        {"username": "jane_doe", "email": "jane.doe@example.com", "age": 25},
    ]

    for u in users_data:
        existing_user = User.query.filter_by(username=u["username"]).first()
        if existing_user is None:
            new_user = User(username=u["username"], email=u["email"], age=u["age"])
            db.session.add(new_user)

    db.session.commit()  # Commit so we can reliably get IDs for posts and comments

    # Retrieve user IDs for convenience
    admin = User.query.filter_by(username='admin').first()
    regular_user = User.query.filter_by(username='user').first()
    john_doe = User.query.filter_by(username='john_doe').first()
    jane_doe = User.query.filter_by(username='jane_doe').first()

    # Posts data to insert
    posts_data = [
        {
            "user_id": admin.id,
            "posted": datetime.strptime("5 November 2021", "%d %B %Y"),
            "title": "Hello World!",
            "body": "This is the first post on this blog."
        },
        {
            "user_id": admin.id,
            "posted": datetime.strptime("17 November 2021", "%d %B %Y"),
            "title": "Post Number two",
            "body": "This is the second post on this blog."
        },
        {
            "user_id": regular_user.id,
            "posted": datetime.utcnow(),
            "title": "Post number three",
            "body": "This is the third post on this blog."
        },
        {
            "user_id": john_doe.id,
            "posted": datetime.utcnow(),
            "title": "A day in the life of John Doe",
            "body": "John shares his daily routine and insights."
        },
        {
            "user_id": jane_doe.id,
            "posted": datetime.utcnow(),
            "title": "Reflections on Learning",
            "body": "Jane writes about her journey in continuous learning."
        }
    ]

    for p in posts_data:
        existing_post = Post.query.filter_by(user_id=p["user_id"], title=p["title"]).first()
        if existing_post is None:
            new_post = Post(
                user_id=p["user_id"],
                posted=p["posted"],
                title=p["title"],
                body=p["body"]
            )
            db.session.add(new_post)

    db.session.commit()  # Commit so posts have IDs for comments

    # Retrieve some posts to attach comments to
    post_hello = Post.query.filter_by(title="Hello World!").first()
    post_two = Post.query.filter_by(title="Post Number two").first()
    post_three = Post.query.filter_by(title="Post number three").first()

    # Comments to insert
    comments_data = [
        {
            "user_id": regular_user.id,
            "post_id": post_hello.id,
            "body": "Great start! Looking forward to more posts."
        },
        {
            "user_id": admin.id,
            "post_id": post_hello.id,
            "body": "Thanks for the feedback!"
        },
        {
            "user_id": jane_doe.id,
            "post_id": post_two.id,
            "body": "Interesting perspective. Keep it up!"
        },
        {
            "user_id": john_doe.id,
            "post_id": post_three.id,
            "body": "I love this post! Very insightful."
        }
    ]

    for c in comments_data:
        existing_comment = Comment.query.filter_by(
            user_id=c["user_id"],
            post_id=c["post_id"],
            body=c["body"]
        ).first()
        if existing_comment is None:
            new_comment = Comment(
                user_id=c["user_id"],
                post_id=c["post_id"],
                body=c["body"],
                posted=datetime.utcnow()
            )
            db.session.add(new_comment)

    db.session.commit()

    print("Database populated successfully!")
