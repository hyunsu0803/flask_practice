from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# 전역 변수
db = SQLAlchemy()
migrate = Migrate()


def create_app():   # 이것이 application factory. flask 내부에서 정의된 함수명이라 이름 바꾸면 동작 안함.

    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blue print
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
