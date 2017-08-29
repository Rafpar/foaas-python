from flask import Flask
from flask import redirect
import random

application = Flask(__name__)


@application.route("/")
def hello():

    ramdomList1 = ["Artless", "Bawdy", "Beslubbering"]
    randomList2 = ["Base-court", "Bat-fowling", "Beef-witted"]
    randomList3 = ["Apple-john", "Baggage", "Barnacle"]
    vowels = "AEIOU"
    article = "a"

    firstWord = random.choice(ramdomList1)
    secondWorld = random.choice(randomList2)
    thirdWord = random.choice(randomList3)
    for x in vowels:
        if firstWord[0] == x:
            article = "an"
    print "Thou art {0} {1} {2} {3}!".format(article, firstWord, secondWorld, thirdWord)


if __name__ == "__main__":
    application.run()

