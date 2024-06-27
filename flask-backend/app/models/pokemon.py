from ..models import db
import enum

class Types(enum.Enum):
    fire ="fire"
    electric ="electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water = "water"
    bug = "bug"
    dragon = "dragon"
    grass = "grass"
    fighting = "fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock= "rock"
    steel = "steel"

class Pokemon(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable = False, unique=True)
    type = db.Column(db.Enum(Types), nullable=False)
    moves = db.Colum(db.String(255), nullable=False)
    encouterRate = db.Column(db.Float, precision=3, decimal_return_scale= 2)
    catchRate = db.Column(db.Float, precision=3, decimal_return_scale= 2)
    captured = db.Column(db.Boolean)

    items = db.relationship('Item', back_populates='pokemon')

    def to_dict(self):
        items = [x.get_id() for x in self.items]
        return {
            'imageUrl':self.imageUrl,
            'id':self.id,
            'number':self.number,
            'name':self.name,
            'captured':self.captured,
            'attack':self.attack,
            'defense':self.defense,
            'type':self.type,
            'items':items
        }
