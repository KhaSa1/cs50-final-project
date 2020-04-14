import os
import requests
import urllib.parse

from datetime import datetime, timedelta
from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(country):
    """Look up covid-19 stats for country."""

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country":country}
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        info = response.json()
        info = info['data']['covid19Stats']
        data = {"confirmed": 0, "deaths": 0, "recovered": 0}
        data["country"] = info[0]["country"]
        data["lastUpdate"] = info[0]["lastUpdate"]
        for i in info:
            data["confirmed"] += i["confirmed"]
            data["deaths"] += i["deaths"]
            data["recovered"] += i["recovered"]
        return {
            "Country": data["country"],
            "Confirmed": data["confirmed"],
            "Deaths": data["deaths"],
            "Recovered": data["recovered"],
            "Last Update": data["lastUpdate"]
        }
    except (KeyError, TypeError, ValueError):
        return None

def totals():

    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    d = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    querystring = {"date":d}

    try:
        api_key = os.environ.get("API_KEY")
        headers = {
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
            'x-rapidapi-key': api_key
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

    except requests.RequestException:
        return None

    # Parse response
    try:
        data = response.json()
        data = data['data']
        data["date"] = d
        return {
            "Total confirmed": data["confirmed"],
            "Total Deaths": data["deaths"],
            "last Updated": data["date"]
        }
    except (KeyError, TypeError, ValueError):
        return None


