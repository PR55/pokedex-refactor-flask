from flask import Flask, Blueprint, render_template, redirect, request
from flask_migrate import Migrate
from ..forms import CreatePokemonForm, ItemForm
from ..models.pokemon import Pokemon, db, Types
from ..models.item import Item
from random import random
from ..seedData import randomImage
bp = Blueprint("pokemons", __name__, url_prefix="/api")


@bp.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    form = CreatePokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        f = ", "
        moves = f.join([form.data["move1"], form.data["move2"]])
        new_pokemon = Pokemon(
            number = form.data["number"],
            attack = form.data["attack"],
            defense = form.data["defense"],
            imageUrl = form.data["imageUrl"],
            name = form.data["name"],
            type = form.data["type"],
            moves = moves
        )
        db.session.add(new_pokemon)
        db.session.commit()
        return new_pokemon.to_dict_no_item()

    if form.errors:
        return form.errors

    all_pokemon = [x.to_dict_no_item() for x in Pokemon.query.all()]
    return all_pokemon

@bp.route("/pokemon/<int:id>", methods=['GET'])
def one_pokemon(id):

    poke = Pokemon.query.filter_by(id = id).first()
    return poke.to_dict_no_item()

@bp.route('/pokemon/<int:id>', methods=["PUT"])
def edit_pokemon(id):
    pokemon = Pokemon.query.filter_by(id = id).first()
    form = CreatePokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    f = ", "
    moves = f.join([form.data["move1"], form.data["move2"]])

    if form.validate_on_submit():
        pokemon.number = form.data["number"]
        pokemon.attack = form.data["attack"]
        pokemon.defense = form.data["defense"]
        pokemon.imageUrl = form.data["imageUrl"]
        pokemon.name = form.data["name"]
        pokemon.type = form.data["type"]
        pokemon.moves = moves

        db.session.commit()

        return pokemon.to_dict_no_item()
    if form.errors:
        return form.errors


@bp.route("/pokemon/types", methods=["GET"])
def get_types():
    return [x.value for x in Types]


@bp.route('/pokemon/random', methods=["GET"])
def get_random():
    pokemon = Pokemon.query.all()
    random_poke = random.choice(pokemon)
    return random_poke.to_dict_no_item()

@bp.route('/pokemon/<int:id>/items', methods=['GET'])
def items(id):
    print(id, "ID")
    items = [x.to_dict() for x in Item.query.filter_by(pokemonId = id).all()]
    return items

@bp.route('/pokemon/<int:id>/items', methods=["POST"])
def post_items(id):
    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_item = Item(
            happiness = form.data["happiness"],
            imageUrl = randomImage(),
            name = form.data["name"],
            price = form.data["price"],
            pokemonId = id
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item.to_dict()
    if form.errors:
        return form.errors
