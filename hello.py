from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import string

app = Flask(__name__, template_folder="/vagrant")

def include(filename):
    if os.path.exists(filename): 
      exec(open(filename).read())
	
@app.route("/")
def index():
    return render_template('index.html')
	
include("success.py")

include("buyticket.py")
include("RateShowing.py")
include("viewedmovies.py")
include("myseenmovies.py")
include("profile.py")
include("personalprofile.py")
include("vul_profile.py")
include("search.py")
include("searchresult.py")

include("movies.py")
include("genres.py")
include("rooms.py")
include("showings.py")
include("customer.py")
include("attend.py")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
	