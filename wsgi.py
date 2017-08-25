from flask import Flask
import applyfuck

application = Flask(__name__)

@application.route("/")
def hello():
    return applyfuck.applyapp()

if __name__ == "__main__":
    application.run()