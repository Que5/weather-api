from flask import Flask, render_template

app = Flask(__name__)


#You can duplicate this function if you want to add more pages, you would cahnge the route and template
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)





