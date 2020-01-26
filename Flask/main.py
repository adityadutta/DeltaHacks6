from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/design-team")
def design_team():
    return render_template("design-team.html")

@app.route("/visuals")
def visuals():
    return render_template("visuals.html")

if __name__ == "__main__": #This allows you to run flask in debug mode through cmd by typing
    app.run(debug=True)		#python main.py I'm going to use the virtual environment instead.

    #Run this code in cmd prompt as admin. change to this file directory. make sure flask is installed
    #try python main.py and hit enter.