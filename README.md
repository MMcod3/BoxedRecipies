## Boxed Recipes

An application that uses Python and a flask framework on the back-end, and materialize framework on the front-end. The application deals manages non-relational data through a database called MongoDB.

This application is an online cookbook that allows users to login or register, create, locate, display, edit and delete recipes.

The live project can be viewed [here](https://boxed-recipies.herokuapp.com/)

### UX

Users are able to view recipes stored on a database, search and filter by cuisine for specific recipes. Users are able to register an account, sign in and sign out. Signed in users are able to add new recipes, edit their own recipes and remove recipes they have shared.

##### User Stories:

- view all recipes stored on the database
- search for a specific recipe
- filter recipes by cuisine
- register on the site
- sign in and sign out
- add new recipes
- edit their recipes
- delete their recipe
- view an specific recipe
- list of recipe instructions
- list of recipe ingredients
- states if any allergens

The site was initially designed using wireframes which were hand drawn. 

### Features

1. **View all recipes-** the initial page of the site allows users to view a list of all recipes currently on the database for the site. Each recipe card has a view button which redirects users to a page for a single recipe where further details of the recipe can be seen such as: allergens, ingredients, method and Author.

2. **Registration/Login-** users are required to create a unique username and password. passwords are hashed user passwords which are not stored in database as simple string text and therefore passwords can't be viewed on the database. Users will be places in session cookies and have authorisation for further features such adding recipes, updating their recipe and deleting their recipe. The registration/login forms use html validation to ensure they match the correct format

3. **Creating, Updating and Deleting recipes-** Logged in users are able to create recipes on seperate page via a form with the use of text inputs, checkboxes and select elemtns and also dynamically add methods and ingredients. Updating recipes redirects users to the same create page, however input elemtns already have the original value.

### Technologies Used

- HTML5 
- CSS
- Python
- jQuery/JavaScript
- Materialize
- Flask
- Flask-PyMongo
- MongoDB

### Testing

Chromes Developer Tools was used to frequently test the responsiveness of the application on different view port sizes. The site was also viwed on a samsung galaxy s21 mobile device with good responsiveness. The site was tested on Mozilla Firefox (71.0), Internet explorer (11.0), Google Chrome (98.0) and all showed correct functionaity and structure. Regular print and console.log statements were used for Python and Javascript respectively, to ensure correct functionality and logic.

All HTML 5 and CSS code was checked through [W3C Validation Tool](https://jigsaw.w3.org/css-validator/) and all codes passed without any errors.

### Deployment

Code was developed on gitpod workspaces and pushed to the github repository for version control through out the application

The live application was then deployed to Heroku. After creating a heroku repository, environment variables were set on heroku and making sure the env.py file was place the gitignore file so sensitive information like passwords and secret keys weren't pushed to heroku. a requirements.txt and procfile file was created.

### Credits

- [Materialize:](https://materializecss.com/) used throughout for projects appearence and responsiveness 
- [Task Manager:](https://github.com/Code-Institute-Solutions/TaskManagerAuth) assisted with the routing and Authorisation
