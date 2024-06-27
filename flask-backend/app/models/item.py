from . import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    happiness = db.Column(db.Integer)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey('pokemons.id'), nullable=False)

    pokemon=db.relationship('Pokemon', back_populates='items')

    def to_dict(self):
        return{
            'id':self.id,
            'happiness':self.happiness,
            'imageUrl':self.imageUrl,
            'name':self.name,
            'price':self.price,
            'pokemonId':self.pokemonId,
        }

    def get_id(self):
        return self.id


