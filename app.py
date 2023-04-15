from flask import Flask, render_template, url_for, request, Response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__, static_folder="static")

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="::")