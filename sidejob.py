from flask import Flask, jsonify
from sqlalchemy import text
from config import Config
from extensions import db, jwt
from blueprints import auth_bp
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")

    # Health Check
    @app.route("/health", methods=["GET"])
    def health_check():
        try:
            # Check database connection
            with db.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return jsonify({"status": "healthy"}), 200
        except Exception as e:
            return jsonify({"status": "unhealthy", "reason": str(e)}), 500

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
