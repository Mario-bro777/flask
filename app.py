from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/search")
def search():
    quest = request.args.get("q")
    return redirect(f"https://www.google.com/search?q={quest}")

@app.get("/json")
def json():
    arg = request.args.get("name")
    if not arg:
        return jsonify({"status":"error", "data":"wrong parameter"})
    return jsonify({"status":"success", "data":f"your request is {arg}"})