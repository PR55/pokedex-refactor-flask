from flask import Flask, Blueprint, render_template, redirect, request
from flask_migrate import Migrate
from ..forms import CreatePokemonForm
from ..models.pokemon import Pokemon, db, Types

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

    if form.errors:
        return form.errors

    all_pokemon = [x.to_dict() for x in Pokemon.query.all()]
    return all_pokemon


@bp.route('/pokemon/<int>:id', methods=["PUT"])
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

        return pokemon
    if form.errors:
        return form.errors
    

@bp.route("/pokemon/types", methods=["GET"])
def get_types():
    return [x.value for x in Types]

