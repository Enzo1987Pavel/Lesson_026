import logging


def create_logger():
	logger = logging.getLogger("basic_log")
	logger.setLevel("INFO")

	file_log_api = logging.FileHandler("logs/api.log")
	logger.addHandler(file_log_api)

	log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
	file_log_api.setFormatter(log_format)

	return logger
