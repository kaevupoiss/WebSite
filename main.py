from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/challenges")
def challenges_page():
    return render_template("challenges.html")

@app.route("/leaderboards")
def leaderboards_page():
    return render_template("leaderboards.html")

@app.route("/forum")
def forum_page():
    return render_template("forum.html")

@app.route("/rules")
def rules_page():
    return render_template("rules.html")

@app.route("/staff")
def staff_page():
    return render_template("staff.html")

@app.route("/store")
def store_page():
    return render_template("store.html")


app.debug = True
app.run()
