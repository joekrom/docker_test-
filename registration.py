from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "that is the service for registration first version herve likes energy drink,first modif to github"

if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True )
