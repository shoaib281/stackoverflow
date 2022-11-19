from flask import Flask
from flask import render_template
from flask import request
from flask import session

from backend import stocks

stocksManager = stocks()

app = Flask(__name__)
app.secret_key = "thisthe secret key"


@app.route("/", methods=["GET"])
def hello_word():
    if not "stocks" in session:
        session["stocks"] = {
            "aapl": {
                "url": "aapl.png"
            },
            "msft":
            {
                "url": "msft.png"
            }
        }

    return render_template("index.html", stocks=session["stocks"])

@app.route("/", methods=["POST"])
def hello_world():
    data = request.form
    ticker = request.form["ticker"]

    stocksManager.generateGraph(ticker) 


    filename =  ticker + ".png" 

    oldDict = session["stocks"]
    oldDict[ticker] = {"url": filename}

    session["stocks"] = oldDict

    return render_template("index.html", stocks=session["stocks"])
