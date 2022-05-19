import logging

from flask import Blueprint, jsonify

from app.posts.DAO.posts_dao import PostsDAO

api_blueprint = Blueprint("api_blueprint", __name__)
posts_DAO = PostsDAO("data/posts.json")


logger = logging.getLogger("basic_log")


@api_blueprint.route("/api/posts/")
def posts_main():
    logger.info("Выполнен запрос всех постов через API (/api/posts/)")
    post_all = posts_DAO.get_posts_all()
    return jsonify(post_all)


@api_blueprint.route("/api/posts/<int:post_pk>/")
def posts_only_one(post_pk):
    logger.info(f"Выполнен запрос поста {post_pk} через API (/api/posts/{post_pk}/)")
    post_all = posts_DAO.get_post_by_pk(post_pk)
    return jsonify(post_all)
