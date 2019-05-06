from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Prueba para AISI"

if __name__ == "__main__":
    application.run()
