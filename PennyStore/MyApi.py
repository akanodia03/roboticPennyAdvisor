from flask import Flask
app = Flask(__name__)

@app.route("/home")
def getDashboard():
    return "Welcome to home page"

@app.route("/about")
def getDetails():
    return "What do you want from me"

if __name__=="__main__":
    app.run(debug=True)