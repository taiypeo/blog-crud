from . import app
from .models import BlogPost

from flask import render_template, abort, redirect, url_for


@app.route("/")
def index():
    return redirect(url_for("index_paged", page=1))


@app.route("/<page>")
def index_paged(page: int):
    try:
        page = int(page)
    except ValueError:
        abort(404)

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
        pagination_target="index_paged",
    )
