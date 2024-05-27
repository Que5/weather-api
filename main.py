from flask import Flask, render_template

app = Flask("Website")

#You can duplicate this function if you want to add more pages, you would cahnge the route and template
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)

