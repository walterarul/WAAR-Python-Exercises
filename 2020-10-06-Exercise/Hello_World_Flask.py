#Exercise 06 October 2020
from flask import Flask
app = Flask(__name__)

@app.route('/')
def login_page():
    return 'Hello World'

#Run/Start the server in debug mode
if __name__ == "__main__":
    app.run(debug=True)
