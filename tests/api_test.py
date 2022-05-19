import pytest

from main import app
from app.posts.DAO.posts_dao import PostsDAO


class TestPostsDAO:

	@pytest.fixture()
	def posts_dao(self):
		return PostsDAO("data/posts.json")

	# Тестируем все посты
	def test_get_all_posts_check(self, posts_dao):
		posts = posts_dao.get_posts_all()
		response = app.test_client().get("/api/posts", follow_redirects=True)

		assert response.status_code == 200, "Для всех постов получен неверный код"
		assert type(posts) == list, "Список постов должен быть списком"

		first_items = posts[0]
		excepted_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
		first_items_keys = set(first_items.keys())
		assert first_items_keys == excepted_keys, "Полученные ключи неверны!"

	# Тестируем один пост
	def test_app_one_posts_status_code(self, posts_dao):
		posts = posts_dao.get_posts_all()
		response = app.test_client().get("/api/posts/1", follow_redirects=True)

		assert response.status_code == 200, "Для всех постов получен неверный код"
		assert type(posts[0]) == dict, "Каждый пост должен быть словарем"

		first_items = posts[0]
		excepted_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
		first_items_keys = set(first_items.keys())
		assert first_items_keys == excepted_keys, "Полученные ключи неверны!"
