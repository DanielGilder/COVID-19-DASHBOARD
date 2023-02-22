import ast,  sched, time
from uk_covid19 import Cov19API
import sched, time,random, os
from covid_news_handling import *
import pickle

def parse_csv_data(csv_filename):
    with open(csv_filename, "r") as file:
        data = file.read()
        rows = data.split("\n")
        del(rows[639])
        
    return rows


def process_covid_csv_data(covid_csv_data):

    #new_data = covid_csv_data[1].split(",")
    #current_hospital_cases = new_data[5]
    last7days_cases = 0
    rowNumber = 1
    count = 0

    print(covid_csv_data[1].split(","))
    for i in range(1,len(covid_csv_data)):
        row = covid_csv_data[i].split(",")
        if row[4] != "":
            total_deaths = int(row[4])
            break


    """   
    for j in range(1, len(covid_csv_data)):
        row = covid_csv_data[j].split(",")


        if row[6] != '':
            last7days_cases =+ int(row[6], base=10)
            
            print("newcasesBySpecimenDate:" + row[6])
            if count == 6:
                break
            else:
                count += 1
    
    
    while(True):





        row = covid_csv_data[rowNumber].split(",")
        

        if row[6] != "":
            last7days_cases =+ int(row[6], base=10)
            dayCount += 1
            rowNumber += 1
            if dayCount == 7:
                print(last7days_cases)
                break
     """
    

    for i in range(2,9):
        row = covid_csv_data[i].split(",")
        last7days_cases += int(row[6])
    
    for i in range(1,len(covid_csv_data)):
        row = covid_csv_data[i].split(",")
        if row[5] != "":
            hospitalCases = int(row[5])
            break



    return last7days_cases, hospitalCases, total_deaths
        

def covid_API_request(update_name,location="Exeter", location_type="ltla"):
   
    england_only = [
    'areaType='+location_type,
    'areaName='+location
    ]

    cases_and_deaths = {

    "date": "date",
    "areaName": "areaName",
    "areaType" : "areaType",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
        }

    api = Cov19API(filters=england_only, structure=cases_and_deaths)
    
    data0 = api.get_dataframe()
    
    data = api.get_csv()
    rows = data.split("\n")
    del(rows[0])
    
    #print(rows)
    test = {'areaName' : {}, 'date' : {}, 'areaType' : {}, 'areaCode' : {}, 'cumDailyNsoDeathsByDeathDate' : {}, 'hospitalCases' : {}}


    for i in range(0, 7):
        row = rows[i].split(",")
        test["areaName"][i] = row[1]
        test["date"][i] = row[0]
        test["areaType"][i] = row[2]
        test['areaCode'][i] = row[3]
        test["cumDailyNsoDeathsByDeathDate"][i] = row[6]       
        test["hospitalCases"][i] = row[4]
    #print(test["date"][0])
    #return test
    #test['areaName'].append(1)
    
    label_and_update = [update_name, test]

    f = open("output_from_data_server.txt", "w")
    f.write(str(label_and_update))
    f.close
    
    
        


scheduler = sched.scheduler(time.time, time.sleep)


def schedule_covid_updates(update_interval=0, update_name="", update_articles="", update_covid_data=""):

    
    if update_covid_data == "covid-data":
        scheduler.enterabs(update_interval, 1, covid_API_request, (update_name))
        scheduler.run(blocking=False)
    if update_articles == "news":
        scheduler.enterabs(update_interval, 1, update_news)
        scheduler.run(blocking=False)



def test():
    l = covid_API_request()
    f = open("output_from_data_server.txt", "w")
    f.write(str(l))
    f.close
    #for writing the api data to the server


    file = open("output_from_data_server.txt")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    print(dictionary["date"][1] + " " + dictionary["areaName"][2] + " "+ dictionary["hospitalCases"][2])
    #for retreiving the api data on the webserver to be displayed


 