from flask import Flask, Response, json
from app.views.redflags_views import redflag_blueprint

def  create_app():
    app = Flask(__name__)
    app.register_blueprint(redflag_blueprint, url_prefix="/api/v1/redflags")
    return app