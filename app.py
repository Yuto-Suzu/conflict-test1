from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template

app = Flask(__name___)

@app.route("/")
def top_page():
    return render_template("index.html")

if __name___ == "___main___":
    app.run(debug=True)