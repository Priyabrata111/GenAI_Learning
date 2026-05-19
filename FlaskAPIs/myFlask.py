from flask import Flask

app = Flask(__name__)

@app.route("/sayhello")
def sayHello():
  return "Hello"


@app.route("/sayhi")
def sayHi():
  return "HI"

app.run()
