from flask import Flask
from flask import redirect
import applyfuck

application = Flask(__name__)


@application.route("/")
def hello():
    return redirect(str(applyfuck.applyapp()))


if __name__ == "__main__":
    application.run()