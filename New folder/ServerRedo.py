import random
import pickle
from flask import Flask, render_template, request, url_for
from covid_data_handler import *
from time_conversion import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    Time = request.args.get('update')
    label = request.args.get("two")
    news = request.args.get("news")
    covid_data = request.args.get("covid-data")

    if Time and label:
        time_interval = hhmm_to_seconds(Time) - time.time()
        if not news and not covid_data:
            schedule_covid_updates(update_interval=time_interval,update_name=label)

        elif news and covid_data:
            schedule_covid_updates(update_interval=time_interval, update_name=label, update_articles= news, update_covid_data=covid_data)

        elif not news and covid_data:
            schedule_covid_updates(update_interval=time_interval,update_name=label, update_covid_data=covid_data)

        elif not covid_data and news:
            schedule_covid_updates(update_interval=time_interval,update_name=label, update_articles=news)


    return render_template("index.html")


if __name__ == "__main__":
    app.run()

