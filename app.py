from flask import Flask

app = Flask(__name__)

@app.route("/loaderio-8af4b41fc4ce9e9fa0c64171bbcdedba", methods=["GET"])
@app.route("/loaderio-8af4b41fc4ce9e9fa0c64171bbcdedba.txt", methods=["GET"])
@app.route("/loaderio-8af4b41fc4ce9e9fa0c64171bbcdedba.html", methods=["GET"])
def loaderIO():
    return "loaderio-8af4b41fc4ce9e9fa0c64171bbcdedba"


if __name__ == "__main__":
    app.run(port=25565)