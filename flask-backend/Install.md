# Pokedex Backend

## How to start

### Setup the database
1. Run `pipenv install` in the flask backend rout for all required dependencies
2. Look at `.env.example` for enviromental variables to add to a new `.env` file
3. In the root directory of the flask backend, run `pipenv run flask db upgrade` to prep the database
4. Run `pipenv run python pokedex_seed.py` to seed the database
5. Run `pipenv run flask run` to start the back end!
