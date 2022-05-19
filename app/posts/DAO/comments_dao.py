import json


class CommentsDAO:

	def __init__(self, path):
		self.path = path

	def load_all_comments(self):
		"""Загрузка всех комментариев из JSON-файла"""
		with open(self.path, "r", encoding="utf-8") as file:
			return json.load(file)

	def get_comment_by_pk(self, post_pk):
		"""Возвращает один комментарий по его идентификатору (post_pk)"""
		comments = self.load_all_comments()
		comments_by_pk = []

		for comment in comments:
			if comment["post_id"] == post_pk:
				comments_by_pk.append(comment)
		return comments_by_pk
