from flask import Flask, render_template, request
import sched, time


from covid_data_handler import *
from covid_news_handling import *

app = Flask(__name__)


def hhmmss_to_seconds( hhmmss: str ) -> int:
      if len(hhmmss.split(':')) != 3:
          print('Incorrect format. Argument must be formatted as HH:MM:SS')
          return None
      return minutes_to_seconds(hours_to_minutes(hhmmss.split(':')[0])) + \
          minutes_to_seconds(hhmmss.split(':')[1]) + int(hhmmss.split(':')[2])



def hhmm_to_seconds( hhmm: str ) -> int:
      if len(hhmm.split(':')) != 2:
          print('Incorrect format. Argument must be formatted as HH:MM')
          return None
      return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
          minutes_to_seconds(hhmm.split(':')[1])

def minutes_to_seconds( minutes: str ) -> int:
      """Converts minutes to seconds"""
      return int(minutes)*60

def hours_to_minutes( hours: str ) -> int:
      """Converts hours to minutes"""
      return int(hours)*60

def current_time_hhmm():
    return str(time.gmtime().tm_hour) + ":" + str(time.gmtime().tm_min)


@app.route("/")
@app.route("/index")
def main():
    text_feild = request.args.get('two')
    if text_feild:
        update_time = request.args.get('update')
        repeat = request.args.get('repeat')
        news = request.args.get('news')
        if repeat != "":
            while True:
                schedule_covid_updates( (hhmm_to_seconds(update_time) - current_time_hhmm()),text_feild)
                return render_template("index.html",)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()