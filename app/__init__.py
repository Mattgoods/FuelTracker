from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Include this to avoid circular imports
    from app import routes

    return app
