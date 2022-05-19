import json


class PostsDAO:

	def __init__(self, path):
		self.path = path

	def get_posts_all(self):
		"""Загрузка всех постов из JSON-файла"""
		with open(self.path, "r", encoding="utf-8") as file:
			return json.load(file)

	def get_posts_by_user(self, user_name):
		"""Возвращает посты определенного пользователя (user_name)"""
		posts = self.get_posts_all()
		posts_by_user_name = []

		for post in posts:
			if post["poster_name"] == user_name:
				posts_by_user_name.append(post)
		return posts_by_user_name

	def search_for_posts(self, query):
		"""Возвращает список постов по ключевому слову"""
		posts = self.get_posts_all()
		searching_posts = []

		for post in posts:
			if query.lower() in post["content"].lower():
				searching_posts.append(post)
		return searching_posts

	def get_post_by_pk(self, pk):
		"""Возвращает один пост по его идентификатору (pk)"""
		posts = self.get_posts_all()

		for post in posts:
			if post["pk"] == pk:
				return post
