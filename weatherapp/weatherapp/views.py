"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from weatherapp import app
from flask import Flask
import os
import json
import time
import urllib2

#
# get_weather calls the API for open weather map organization DB, and fetch the result. 
# As the weather information is not changed much or quickly, it is not necessary to query often.
#
def get_weather():
    url="http://api.openweathermap.org/data/2.5/forecast/city?id=4255818&APPID=54e5b332a6ac1a0c9d2f2677cd8b289e"
    response = urllib2.urlopen(url).read()
    return response

#
# This is the main module to call the API, and return the values on the html file.
#
@app.route('/')
@app.route('/home')
def index():
    data = json.loads(get_weather())
    page = "<html><head><title>Clark County Wether</title></head><body>"
    page += "<h1>Wather for {}, {}</h1>".format(data.get('city').get('name'), data.get('city').get('county'))
    
    for day in data.get("list"):
        page += "<b>date:</b> {} <b>min:</b> {} <b>max:</b> {} <b>description:</b> {} <br />".format(
                time.strftime('%d %B', time.localtime(day.get('dt'))),
                (day.get("main").get("temp_min")),
                day.get("main").get("temp_max"),
                day.get("weather")[0].get("description"))
    page += "</body></html>"
    return page

#
# Simple saying goodbye
#

@app.route("/goodbye")
def goodbye():
    return "Goodbye, World"

#
# another example to print out the name and age per input.
#
@app.route("/hello/<name>/<int:age>")
def hello_name(name,age):
    return "Hello, {}, you are {} years old".format(name, age)

#
# built-in contact
#
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

#
# built-in about
#
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
