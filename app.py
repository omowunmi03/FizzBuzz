from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def fizzbuzz():
    return render_template("fizzbuzz.html")