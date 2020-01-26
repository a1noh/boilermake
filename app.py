#!flask/bin/python
from flask import Flask, current_app

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"
    #return current_app.send_static_file('homepage.html')

if __name__ == "__main__":
    app.run(debug=True, port=9999)