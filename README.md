# CS50 Final Project

This project is a web app that shows coronavirus statistics.
users can play a quiz if he/she clicks in the logo button.
The user must register then login to unlock the search country stats and prevention tips features.
when the user login, he can change his profile settings (username, password) and can save his/her and unsave tips.

you can alter tips.csv but you have to update the database with the new data so run in cmd:
python import.py tips.csv

# usage
register and login to rapid api for api key then run on the command-line:

## for mac and linux
cd [path to app.py] <br/>
export API_KEY=[your api key] <br/>
export FLASK_APP=app.py <br/>
flask run <br/>
### optional
export FLASK_ENV=development <br/>
export FLASK_DEBUG=1 <br/>

## for Windows
cd [path to app.py] <br/>
set API_KEY=[your api key] <br/>
set FLASK_APP=app <br/>
flask run
### optional
set FLASK_ENV=development <br/>
set FLASK_DEBUG=1
<br/>
for more info visit: https://flask.palletsprojects.com/en/1.0.x/cli/



