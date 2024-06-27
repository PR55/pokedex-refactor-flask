# FLASK - REACT Refactor Project!

This project is meant to give you practice working with a Flask server and a React client.  The `backend` and `frontend` folders contain the solution code to the Pokedex project you completed in Module 5

Your tasks for today are the following:

1. Create a Flask server to replace the express server.  The code to inject CSRF tokens into every response is included in the `flask-backend` folder, along with a pipfile with many of the dependaecies you will need. You will also need to add the line of code below in your post routes, after you instantiate a form but before you check for the `validate_on_submit` to trick WTForms of a valid csrf token. It is your task to code out the rest of the flask backend.
```python
 form['csrf_token'].data = request.cookies['csrf_token']
```


2. You are not allowed to change any of the code in the frontend folder.  You need to make your Flask server work with the existing React client.  You may add `console.log()` statements to help you debug, and you may refactor code in the thunks if needed (like destructuring or data manipulation), but that is it.

3. Flask server will require the following:

    a. 3 models, Pokemon, PokemonType, and Item with all the same relationships and constraints as the express server

    b. Routes to hande full CRUD for Items and CR functionality for Pokemon (same as the express server)

    c. Server side validation on all data that can be validated with the built-in validators in WTforms (DataRequired, Length, NumberRange, URL) https://wtforms.readthedocs.io/en/2.3.x/validators/

    d. You will need to make a seed file, it does not need to have all the data from the original project, but there should be 15 seeded Pokemon, 10 seeded Items, and all of the same PokemonTypes as the express server 

    e. React frontend must have all the same functionality it did when it was connecting to the express server.

    f. The way the Pokemon `moves` attribute is set up is a bit wonky, as moves is really a list/array, but it is being saved as a string. Feel free to save it as string in your flask backend as well (maybe with commas seperated values that you can split/join as needed?) 

4. There is no solution file for this project!  (“No! Try not. Do. Or do not. There is no try.” - Master Yoda)


## Rules!

1. This will be a project for your project group!  You can all work together, or you can split up in to pairs if you feel that will accomplish more, but ***no solo work***!  Remember to respect each other, you are a team set upon a challenge to acheive a common goal!

2. All debugging questions will go in the online questions channel, using the formal project question asking process you have used in previous project weeks.  If you are not sure about this process, there is a reading in the Module 6 resources folder to reference!  https://github.com/appacademy/Module-6-Resources/blob/main/group_project_resources/question-procedure.md

3. Once you have completed the flask server refactor (and sufficiently tested it) zip the project and submit it to your project advisor for review.  Make sure to include instructions on what we need to do to successfully start up your project!  (like run npm install, or how to run migrations and seed the database)  

4. If you complete the refactor by EOD, your team will get one additional pregrade/feature review during project week.

5. Instructional team may award additional bonus pregrade/feature review rewards at our discretion, like if you implement something really cool that we feel warrants it, so even if you don't finish the project, still submit your code!  (example, set up a random generation script for Item seeding like the original express server does)

6. Have fun!  This is great practice for the upcoming project, and you get to work with your group!

