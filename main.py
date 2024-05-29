from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


#You can duplicate this function if you want to add more pages, you would cahnge the route and template
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station, "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)





