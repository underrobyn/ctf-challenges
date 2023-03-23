from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from passlib.context import CryptContext
import mimetypes


mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')


# Initialise objects
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


# Define folders
static_folder = 'static'
template_folder = 'templates'


def create_app():
    app = Flask(__name__, template_folder=template_folder, instance_relative_config=False, static_folder=static_folder)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from . import routes

        app.register_blueprint(routes.main)

        db.create_all()

    login_manager.login_view = "main.auth"

    @app.after_request
    def apply_headers(response):
        response.headers["Server"] = "TwoFactor"
        response.headers['Cross-Origin-Resource-Policy'] = 'same-site'

        if not request.path.startswith('/static/') and not request.path.startswith('/api/'):
            response.headers["Referrer-Policy"] = "same-origin"
            response.headers["X-Frame-Options"] = "Deny"
            response.headers["X-XSS-Protection"] = "1; mode=block"

            csp_header_value = "script-src 'self' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; img-src 'self' data: blob: https://cdnjs.cloudflare.com https://api.cellmapper.net https://www.three.co.uk/ https://mapserver.vodafone.co.uk https://68aa7b45-tiles.spatialbuzz.net https://coverage.ee.co.uk https://mt1.google.com https://tile.opentopomap.org https://*.tile.openstreetmap.org https://*.api.tomtom.com; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; connect-src 'self' https://analytics.mappr.uk https://nominatim.openstreetmap.org https://mappr.report-uri.com; media-src 'none'; object-src 'none'; child-src 'none'; form-action 'self'; upgrade-insecure-requests; block-all-mixed-content; manifest-src 'self'; worker-src 'self'; report-uri https://mappr.report-uri.com/r/d/csp/reportOnly"

            # Production only headers
            if app.config['ENV'] == 'production':
                response.headers['Content-Security-Policy-Report-Only'] = csp_header_value
                response.headers['Cross-Origin-Embedder-Policy-Report-Only'] = 'require-corp; report-to="default"'
                response.headers['Cross-Origin-Opener-Policy-Report-Only'] = 'same-origin; report-to="default"'

            # Testing headers
            if app.config['ENV'] == 'development':
                response.headers['Content-Security-Policy'] = csp_header_value
                response.headers['Cross-Origin-Embedder-Policy'] = 'unsafe-none; report-to="default"'
                response.headers['Cross-Origin-Opener-Policy'] = 'same-origin; report-to="default"'

        return response

    return app


app = create_app()
