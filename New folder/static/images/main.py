from covid_data_handler import *
from covid_news_handling import *


def test_parse_csv_data ():
    data = parse_csv_data ("nation_2021-10-28-1.csv")
    print(data)
    assert len(data) == 639
    
def test_process_covid_csv_data ():
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data( parse_csv_data("nation_2021-10-28-1.csv"))
   # assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_54
   

#covid_API_request()
#test_parse_csv_data()
news_API_request()