
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .config import Config
from flask import Flask
from .models import db
from .models.item import Item
from .models.pokemon import Pokemon
from flask_migrate import Migrate
import os
from .routes.items import bp as items
from .routes.pokemon import bp as pokemons

app =Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(items)
app.register_blueprint(pokemons)

db.init_app(app)

Migrate(app, db)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

