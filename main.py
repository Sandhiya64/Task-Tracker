from flask import Flask, flash
from config import Config
from extensions import db, migrate
from task.routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(task_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
