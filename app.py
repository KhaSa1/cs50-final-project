import os, time

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, totals

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///covid19.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# search for covid-19 stats for given country
@app.route("/search", methods=["POST"])
@login_required
def search():
    if request.method == "POST":
        country = request.form.get("country")
        res = lookup(country.capitalize())
        total = totals()
        return render_template("result.html", res=res, total=total, country=res['Country'].casefold())

    return apology("Request method is not supported")

# Register into the website
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Reconnect to the database
    db = None
    db = SQL("sqlite:///covid19.db")
    # display registration form if the request is via get
    if request.method == "GET":
        return render_template("register.html")

    # Insert the new user to the database if not registered
    elif request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        """ Check for inavalid inputs """
        if not username:
            return apology("Missing username!")
        elif not email or not ('.' and '@') in email:
            return apology("Missing email!")
        elif not password:
            return apology("Missing password!")
        elif not confirmation:
            return apology("Missing password confirmation!")
        # check if passwords match if not apologize
        elif not password == confirmation:
            return apology("The passwords didn't match!")

        # Query database for username
        user_check = db.execute("SELECT * FROM 'users' WHERE email = :email;", email=email)
        # if this email already exist in the database
        if user_check:
            return apology("This Email is registered!")
        # if the inputs are valid then insert user data into the database ( hashing the password )
        db.execute("INSERT INTO 'users' (username, email, hash) VALUES (:username, :email, :hash)",
                   username=username, email=email, hash=generate_password_hash(password))
        # Query database for user id
        row = db.execute("SELECT id, username FROM 'users' WHERE username = :username", username=username)
        # log in automatically
        if session.get("user_id") is None:
            session["user_id"] = row[0]["id"]
        if session.get("user_id") is None:
            session["user_name"] = row[0]["username"]


        return redirect(url_for('index'))

    # if the request method is neither post nor get, apologise
    return apology("This request method is not supported")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    # Reconnect to the database
    db = None
    db = SQL("sqlite:///covid19.db")
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        email = request.form.get("email")
        # Ensure username was submitted
        if not email:
            return apology("must provide username or email", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for email
        rows = db.execute("SELECT * FROM 'users' WHERE email = :email", email=email)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid email and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["username"]

        # Redirect user to home page
        return redirect(url_for("index"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for('login'))


# Edit profile
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        # Reconnect to the database
        db = None
        db = SQL("sqlite:///covid19.db")

        username = request.form.get("username")
        email = request.form.get("email")
        old_password = request.form.get("o-password")
        new_password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        """ Check for inavalid inputs """
        if not email:
            flash("Missing Email!")
            return redirect( url_for('profile') )
        elif not old_password:
            flash("Missing old password!")
            return redirect( url_for('profile') )
        elif not new_password:
            flash("Missing new password!")
            return redirect( url_for('profile') )
        elif not confirmation:
            flash("Missing password condirmation!")
            return redirect( url_for('profile') )
        # check if passwords match if not apologize
        elif not new_password == confirmation:
            return apology("The passwords didn't match!")

        # Query database for user data
        user_check = db.execute("SELECT * FROM 'users' WHERE id = :id AND email = :email",
                                id=session["user_id"], email=email)
        # Ensure username exists and password is correct
        if len(user_check) != 1 or not check_password_hash(user_check[0]["hash"], old_password):
            return apology("invalid email and/or password", 403)
        #Update user username
        if username:
            flash('Username Changed Successfully!\n')
            db.execute("UPDATE 'users' SET username = :username WHERE id = :id",
                        username=username, id=session["user_id"])
            session["user_name"] = username
        # Update user password
        db.execute("UPDATE 'users' SET hash = :hash WHERE id = :id",
                   hash=generate_password_hash(new_password), id=session["user_id"])
        flash('Password Changed Successfully!')
        return redirect(url_for('profile'))

    elif request.method == "GET":
        return render_template('profile.html', name=session["user_name"])

    return apology("Request method is not supported")


@app.route("/api")
@login_required
def api():
    if request.method == "GET":
        # Reconnect to the database
        db = None
        db = SQL("sqlite:///covid19.db")
        rows = list(db.execute("SELECt * FROM 'tips'"))
        arr = []
        for row in rows:
            data = {"id": row["id"],
                    "tip": row["tip"]
            }
            arr.append(data)
        return jsonify({"tips": arr})

    return apology("Request method is not supported")

@app.route("/tips", methods=["GET", "POST"])
@login_required
def tips():
    # Reconnect to the database
    db = None
    db = SQL("sqlite:///covid19.db")
    if request.method == "GET":
        rows = db.execute("SELECT tip_id, tip, date FROM 'user_tips' \
                           JOIN 'users' ON user_tips.user_id = users.id \
                           JOIN 'tips' ON user_tips.tip_id = tips.id \
                           WHERE users.id = :id ORDER BY tip_id", id=session["user_id"])
        return render_template("tips.html", rows=rows)

    elif request.method == "POST":
        num = request.form.get("num")
        # Check if this tip is already saved in this account
        row = db.execute("SELECT tip_id FROM 'user_tips' \
                          JOIN 'users' ON user_id = users.id\
                          WHERE tip_id = :tip_id AND user_id = :user_id",
                          tip_id=num, user_id=session["user_id"])
        # if so return
        if row:
            return "Already Saved"
        # else save this tip in this account
        db.execute("INSERT INTO 'user_tips' (user_id, tip_id) VALUES (:user_id, :tip_id)",
                    user_id=session["user_id"], tip_id=num)
        return "Successfully Saved"

    return apology("Request method is not supported")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
