# Import all modules
from flask import Flask, jsonify, request
import csv 

# All articles list
all_articles = []

# Put " encoding="utf-8" " in project as well
# Opening the csv file
with open('articles.csv', encoding="utf-8") as f:
    reader = csv.reader(f) # Reading the file
    data = list(reader) # Storing in data
    all_articles = data[1:] # Taking out the first index

# Creating the other lists for liked, and disliked articles
liked_articles = []
disliked_articles = []

# Creating flask
app = Flask(__name__)

# Function for first api
@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "Success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:] # Remove the article from the all articles list
    liked_articles.append(article) # Append the liked article in that list
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:] # Remove the article from the all articles list
    disliked_articles.append(article) # Append the disliked article in that list
    return jsonify({
        "status": "Success"
    }), 201

if __name__ == "__main__":
    app.run()