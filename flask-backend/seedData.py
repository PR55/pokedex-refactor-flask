from random import randint

pokemon_seeds = [
    {
        "number": 1,
        "imageUrl": '/images/pokemon_snaps/1.svg',
        "name": 'Bulbasaur',
        'attack': 49,
        'defense': 49,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip'
        ],
        'captured': True
      },
      {
        "number": 2,
        "imageUrl": '/images/pokemon_snaps/2.svg',
        "name": 'Ivysaur',
        'attack': 62,
        'defense': 63,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        'captured': True
      },
      {
        "number": 3,
        "imageUrl": '/images/pokemon_snaps/3.svg',
        "name": 'Venusaur',
        'attack': 82,
        'defense': 83,
        'type': 'grass',
        'moves': [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        'captured': True
      },
      {
        "number": 4,
        "imageUrl": '/images/pokemon_snaps/4.svg',
        "name": 'Charmander',
        'attack': 52,
        'defense': 43,
        'type': 'fire',
        'moves': [
          'scratch',
          'ember',
          'metal claw'
        ],
        'captured': True
      },
      {
        "number": 5,
        "imageUrl": '/images/pokemon_snaps/5.svg',
        "name": 'Charmeleon',
        'attack': 64,
        'defense': 58,
        'type': 'fire',
        'moves': [
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ],
        'captured': True
      },
      {
        "number": 6,
        "imageUrl": '/images/pokemon_snaps/6.svg',
        "name": 'Charizard',
        'attack': 84,
        'defense': 78,
        'type': 'fire',
        'moves': [
          'flamethrower',
          'wing attack',
          'slash',
          'metal claw'
        ],
        'captured': True
      },
      {
        "number": 7,
        "imageUrl": '/images/pokemon_snaps/7.svg',
        "name": 'Squirtle',
        'attack': 48,
        'defense': 65,
        'type': 'water',
        'moves': [
          'tackle',
          'bubble',
          'water gun'
        ],
        'captured': True
      },
      {
        "number": 8,
        "imageUrl": '/images/pokemon_snaps/8.svg',
        "name": 'Wartortle',
        'attack': 63,
        'defense': 80,
        'type': 'water',
        'moves': [
          'tackle',
          'bubble',
          'water gun',
          'bite'
        ],
        'captured': False
      },
      {
        "number": 9,
        "imageUrl": '/images/pokemon_snaps/9.svg',
        "name": 'Blastoise',
        'attack': 83,
        'defense': 100,
        'type': 'water',
        'moves': [
          'hydro pump',
          'bubble',
          'water gun',
          'bite'
        ],
        'captured': False
      },
      {
        "number": 10,
        "imageUrl": '/images/pokemon_snaps/10.svg',
        "name": 'Caterpie',
        'attack': 30,
        'defense': 35,
        'type': 'bug',
        'moves': [
          'tackle'
        ],
        'captured': False
      },
      {
        "number": 12,
        "imageUrl": '/images/pokemon_snaps/12.svg',
        "name": 'Butterfree',
        'attack': 45,
        'defense': 50,
        'type': 'bug',
        'moves': [
          'confusion',
          'gust',
          'psybeam',
          'silver wind'
        ],
        'captured': False
      },
      {
        "number": 13,
        "imageUrl": '/images/pokemon_snaps/13.svg',
        "name": 'Weedle',
        'attack': 35,
        'defense': 30,
        'type': 'bug',
        'moves': [
          'poison sting'
        ],
        'captured': False
      },
      {
        "number": 16,
        "imageUrl": '/images/pokemon_snaps/16.svg',
        "name": 'Pidgey',
        'attack': 45,
        'defense': 40,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust'
        ],
        'captured': False
      },
      {
        "number": 17,
        "imageUrl": '/images/pokemon_snaps/17.svg',
        "name": 'Pidgeotto',
        'attack': 60,
        'defense': 55,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust',
          'wing attack'
        ],
        'captured': False
      },
      {
        "number": 18,
        "imageUrl": '/images/pokemon_snaps/18.svg',
        "name": 'Pidgeot',
        'attack': 80,
        'defense': 75,
        'type': 'normal',
        'moves': [
          'tackle',
          'gust',
          'wing attack'
        ],
        'captured': False
      },
      {
        "number": 19,
        "imageUrl": '/images/pokemon_snaps/19.svg',
        "name": 'Rattata',
        'attack': 56,
        'defense': 35,
        'type': 'normal',
        'moves': [
          'tackle',
          'hyper fang'
        ],
        'captured': False
      },
      {
        'number': 20,
        'imageUrl': '/images/pokemon_snaps/20.svg',
        'name': 'Raticate',
        'attack': 81,
        'defense': 60,
        'type': 'normal',
        'moves': [
          'tackle',
          'hyper fang'
        ],
        'captured': False
      }
]

def randomImage():
  images = [
    "https://ghostwalker186.wordpress.com/wp-content/uploads/2013/10/potion.png",
    "https://pixelmonmod.com/w/images/4/40/Grid_Pok%C3%A9_Ball.png",
    "https://pixelmonmod.com/w/images/thumb/8/8b/Grid_Pink_Apricorn.png/24px-Grid_Pink_Apricorn.png",
    "https://pixelmonmod.com/w/images/thumb/7/70/Grid_Lum_Berry.png/48px-Grid_Lum_Berry.png",
    "https://pixelmonmod.com/w/images/a/ad/Grid_Leaf_Stone.png"
  ]
  index = randint(0, len(images)-1)
  return images[index]

# for i in range(0, 10):
#   print(randomImage())

def randomProductName():
  p1 = ['Cure', 'Berry',
        'Potion', 'Remedy',
        'Power', 'Wand',
        'Linux', 'Torvalds']
  p2 = ['of', '', 'the', 'Miranda']
  p3 = ['Miracles', 'Healing',
        'Recovery', 'Band',
        'Bracelet', 'Redundancy',
        'Linus']
  choice1 = p1[randint(0, len(p1)-1)]
  choice2 = p2[randint(0, len(p2)-1)]
  choice3 = p3[randint(0, len(p3)-1)]
  if choice2 == '':
    return f'{choice1} {choice3}'
  return f'{choice1} {choice2} {choice3}'

# print(randomProductName())
