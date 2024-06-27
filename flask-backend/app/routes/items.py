from flask import Flask, Blueprint, render_template, redirect, request
from flask_migrate import Migrate
from ..forms import ItemForm
from ..models.item import Item, db

bp = Blueprint("items", __name__, url_prefix="/api")


@bp.route('/items/<int>:id', methods=["PUT"])
def update_item(id):
    item = Item.query.filter_by(id = id).first()
    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        item.happiness = form.data["happiness"]
        item.name= form.data["name"]
        item.price = form.data["price"]
        
        db.session.commit()
        return item
    if form.errors:
        return form.errors


@bp.route('/<int>:id', methods=["DELETE"])
def delete_item(id):
    item = Item.query.filter_by(id = id).first()
    db.session.delete(item)
    db.session.commit()
    return {"id": id}