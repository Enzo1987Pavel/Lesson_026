from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from app.posts.DAO.posts_dao import PostsDAO
from app.posts.DAO.comments_dao import CommentsDAO


posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_DAO = PostsDAO("data/posts.json")
comments_DAO = CommentsDAO("data/comments.json")


@posts_blueprint.route("/")
def posts_main():
    try:
        posts = posts_DAO.get_posts_all()
        return render_template("index.html", posts=posts)
    except AttributeError as error_text:
        title_error = "Ошибка загрузки!"
        return render_template("error_template.html", title_error=title_error, error_text=error_text)


@posts_blueprint.route("/posts/<int:post_pk>/")
def posts_only_one(post_pk):
    try:
        post = posts_DAO.get_post_by_pk(post_pk)
        comments = comments_DAO.get_comment_by_pk(post_pk)

    except (JSONDecodeError, FileNotFoundError) as error_text:
        title_error = "Ошибка загрузки!"
        return render_template("error_template.html", title_error=title_error, error_text=error_text)
    except BaseException as error_text:
        title_error = "Ошибка загрузки!"
        return render_template("error_template.html", title_error=title_error, error_text=error_text)
    else:
        if post is None:
            abort(404, description="Страница не найдена!")
        number_of_comments = len(comments)
        post_pk = posts_DAO.get_post_by_pk(post_pk)

        return render_template("post.html", post=post, comments=comments, number_of_comments=number_of_comments, post_pk=post_pk)


@posts_blueprint.route("/search/")
def posts_search():
    try:
        query = request.args.get("s", "")

        if query != "":
            posts = posts_DAO.search_for_posts(query)
            posts_count = len(posts)
        else:
            posts = []
            posts_count = 0

        return render_template("search.html", query=query, posts=posts, posts_count=posts_count)

    except:
        return "Ошибка при загрузке страницы поиска"


@posts_blueprint.route("/users/<username>/")
def posts_username(username):
    try:
        posts = posts_DAO.get_posts_by_user(username)
        posts_count = len(posts)
        return render_template("user-feed.html", posts=posts, posts_count=posts_count)
    except:
        return "Ошибка при загрузке постов пользователя"
