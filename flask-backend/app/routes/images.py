from flask import Blueprint, url_for

bp = Blueprint("images", __name__, url_prefix="/images")

bp.route('')
def index():
    return 'a'

bp.route('<string:path>')
def image(path):
    return url_for('static', filename=path)
