import flask
import os
from flask import request
posts = []

app = flask.Flask(__name__)
app.config['DEBUG'] = True

port = int(os.environ.get('PORT', 5000))

@app.route('/feed', methods=["GET"])
def feed():
    post = '<br>'.join(posts)
    return post

@app.route('/add_post', methods=["GET"])
def add():
    print(request.query_string)
    post = str(request.query_string)[2:-1]
    posts.append(post)
    return post

app.run(
    host='0.0.0.0',
    port=port
)
