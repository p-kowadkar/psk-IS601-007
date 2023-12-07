# from https://towardsdatascience.com/deploy-to-google-cloud-run-using-github-actions-590ecf957af0
import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name', 'World')
    return f'Hello Pranav!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))