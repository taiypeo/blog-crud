from . import app, db
from .models import BlogPost, User
from .forms import RegistrationForm

from flask import render_template, abort, redirect, url_for, request, flash
from sqlalchemy.exc import DatabaseError


@app.route("/")
def index():
    if "page" not in request.args:
        return redirect(url_for("index", page=1))
    else:
        page = int(request.args["page"])

    pagination = BlogPost.query.order_by(BlogPost.date_created.desc()).paginate(
        page=page
    )
    posts = pagination.items
    total_pages = pagination.pages
    return render_template(
        "posts.html",
        title="My blog website",
        posts=posts,
        current_page=page,
        total_pages=total_pages,
        pagination_target="index",
        url_kwargs={},
    )


@app.route("/u/<id>")
def user(id: int):
    try:
        id = int(id)
    except ValueError:
        abort(404)

    if "page" not in request.args:
        return redirect(url_for("user", id=id, page=1))
    else:
        page = int(request.args["page"])

    user = User.query.get(id)
    if not user:
        abort(404)

    pagination = user.posts.order_by(BlogPost.date_created.desc()).paginate(page=page)
    posts = pagination.items
    total_pages = pagination.pages

    return render_template(
        "posts.html",
        title=f"{user.username}'s posts",
        top_text=f"{user.username}'s posts",
        posts=posts,
        current_page=page,
        total_pages=total_pages,
        pagination_target="user",
        url_kwargs={"id": id},
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))
        except DatabaseError:
            db.session.rollback()

            if User.query.filter_by(username=form.username.data):
                flash("User with this username already exists.")
            else:
                flash("Unknown database error has occurred.")

    return render_template("register.html", form=form)