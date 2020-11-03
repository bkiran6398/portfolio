from flask import Flask, render_template
import json

app = Flask(__name__)

with open('config.json', 'r') as f:
    parameters = json.load(f)['params']


@app.route("/")
def index():
    return render_template('index.html', params=parameters)


if __name__ == "__main__":
    app.run(debug=True)
