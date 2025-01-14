from flask import Flask, render_template, request
import pandas as pd
# from sklearn.metrices.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

if __name__=="__main__":
    app.run(debug=True)