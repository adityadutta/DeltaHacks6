from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": #This allows you to run flask in debug mode through cmd by typing
    app.run(debug=True)		#python main.py I'm going to use the virtual environment instead.