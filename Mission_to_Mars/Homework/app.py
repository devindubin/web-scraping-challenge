from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars



app = Flask(__name__)


####
#Mongo
####
conn="mongodb://localhost:27017/"
client = MongoClient(conn)

#web-scraping-challenge == wsc; declare database
db = client.wsc
#declare collection
mars = db.mars



@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/scrape')
def scrape():
    scraped_dict = scrape_mars.scrape()
    #mars.insert_one(scraped_dict)



if __name__ == "__main__":
    app.run()