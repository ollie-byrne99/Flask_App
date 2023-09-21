# Instructions for Usage

1 - Clone the repo to your device: `git clone https://github.com/ollie-byrne99/Flask_App.git`

2 - Install pipenv to access the scripts and packages for this environment: `pip install pipenv`

3 - Install the package dependencies: `pipenv install`

4 - Create a .env in the repo and add: 
    FLASK_APP=app 
    FLASK_DEBUG=1
    DB_URL= (This must be set to a database url that you create)

4 - Seed the database: `pipenv run setup-db`

5 - Run the server: `pipenv run dev` 
Access at http://localhost:5000/
