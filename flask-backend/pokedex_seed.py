from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models.item import Item
from app.models.pokemon import Pokemon
from random import randint, uniform
from seedData import pokemon_seeds, randomImage, randomProductName

with app.app_context():

    for pokemo in pokemon_seeds:
        s = ', '
        moves = s.join(pokemo['moves'])
        new_pokemon = Pokemon(
            number = pokemo['number'],
            imageUrl = pokemo['imageUrl'],
            name = pokemo['name'],
            attack = pokemo['attack'],
            defense = pokemo['defense'],
            type = pokemo['type'],
            moves = moves,
            catchRate = uniform(0, 100),
            encounterRate = uniform(0,100),
            captured = pokemo['captured'],
        )
        # print(new_pokemon)
        db.session.add(new_pokemon)
    db.session.commit()
    for i in range(1 , len(pokemon_seeds)+1):
        for j in range(0, 3):
            new_item = Item(
                pokemonId = i,
                name = randomProductName(),
                price = randint(1, 100),
                happiness = randint(1,100),
                imageUrl = randomImage()

            )
            # print(new_item.name)
            db.session.add(new_item)
    db.session.commit()
    # print(len(pokemon_seeds))
    # db.session.add()
    # db.session.commit()
