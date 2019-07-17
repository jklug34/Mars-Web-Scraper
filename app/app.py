from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    try:
        mars_data = mongo.db.mars_data.find_one()
        return render_template('index.html', mars_data=mars_data)
    except:
        return redirect("/")


@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape_all()
    mars_data.update({}, mars_data_scrape, upsert=True)

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)