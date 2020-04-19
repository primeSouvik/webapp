from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return("hello, world!")

@app.route("/souvik")
def souvik():
    return ("<h1> hello, souvik </h1>")
