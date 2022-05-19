from flask import Flask, render_template

from app.api.views import api_blueprint
from app.posts.views import posts_blueprint
from app import logger


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

logger.create_logger()

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("error_500.html"), 500


if __name__ == "__main__":
    app.run(debug=False)
