from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Vai tomar no cu Azure"


if __name__ == '__main__':
    app.run()