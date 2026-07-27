from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  pass

app.run(debug=True)
