from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def index():
    w = request.args.get("word")
    return jsonify({"message": f"Your type: {w}"})