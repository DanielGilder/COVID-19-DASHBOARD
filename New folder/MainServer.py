import random
import pickle
from flask import Flask, render_template, request, url_for
from covid_data_handler import *
from time_conversion import *
import logging
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
@app.route("/")
@app.route("/index")
def index():

   o = open('config.json')
   faveIcon = json.load(o)
   Time = request.args.get('update')
   label = request.args.get("two")
   news = request.args.get("news")
   covid_data = request.args.get("covid-data")
   

   
   if label and Time:
      schedule_covid_updates(hhmm_to_seconds(Time) -time.time(),label,news,covid_data)    

      try:
         file = open("output_from_data_server.txt")
         contents = file.read()
         List = ast.literal_eval(contents)
         file.close()

         open_file = open("StoredUpdates.pkl", "rb")
         load = pickle.load(open_file)
         open_file.close()
         load.append({'title' : label, 'content' : Time})


         open_file = open("StoredUpdates.pkl", "wb")
         pickle.dump(load, open_file)
         open_file.close()

         return render_template("index.html",updates=load,title=List['areaName'][0], hospital_cases=List['hospitalCases'][0])

      except:
         print("Continue")
   

   
      

      
   return render_template("index.html", favicon=faveIcon['favicon'])   





if __name__ == "__main__":
    app.run()

