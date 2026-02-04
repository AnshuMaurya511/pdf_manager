from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'YOUR_SECERT_KEY'

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.dirname(BASE_DIR)

    UPLOAD_PATH = os.path.join(PROJECT_ROOT, 'uploads')

    app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
    os.makedirs(UPLOAD_PATH, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:Anshu%40123@localhost/Note_app'
)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.notes import notes_bp
    from app.routes.registers import registers_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(registers_bp, url_prefix='/registers')
    app.register_blueprint(notes_bp, url_prefix='/notes')
    
    @app.route('/')
    def index():
        from flask import redirect, url_for
        return redirect(url_for('auth.login'))
    
    return app

from app import routes