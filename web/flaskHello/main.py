from flask import Flask

application = Flask(__name__)

@application.route("/")

def hello():
    return "Hello World!"

@application.route("/hello")
def helloWorld():
    return "New Page"

if __name__ == '__main__':
    application.run()