from newsapi import NewsApiClient
import json, pickle

def news_API_request(covid_terms="Covid COVID-19 coronavirus"):
    f = open('config.json')
    config = json.load(f)
    newsapi =  NewsApiClient(api_key=config["NEWS_API_KEY"])

    Headlines = newsapi.get_top_headlines(q=covid_terms, language='en')
    
    #print(Headlines["articles"][0]['description'])

    #[ {title : example1, description: some text} , {title2: example2, description: some text} ]
    Headlines_modified = []
    for i in range(0, len(Headlines['articles'] )):
        Headlines_modified.append({'title': Headlines['articles'][i]['title'], 'description' :  Headlines['articles'][i]['description'], 'read' : False})
      
    return Headlines_modified
   





def update_news():
    news = news_API_request() # :=  [{title : "sdzx", description : "sdfsdsd"} , {title : "sdfs", description : "dvsd"} , ....]
    #new structure;  [news, news1, news2, news3, news4]
    #test = [{'title': 'lEspinoza: Christmas, elections and Omicron - Yahoo Philippines News', 'description': 'Our Christmas celebration this year will never be the same as it used to be before this deadly new coronavirus (Covid-19) arrived on our shores. The virus...', 'read': False}]
    open_file = open("stored_news.pkl", "rb")
    News = pickle.load(open_file)
    open_file.close() 
    """
    for new in news:
        for i in range(0, len(News)):
            if new['title'] in News[i]:
                print("This Title has already been stored")
                continue
            else:
                new['read'] = False
                News.append(new)
      """        
       
    for elem in news:
        if elem in News:
            print("This title is already stored")
        
        else:
            News.append(elem)

    #print(News)
    

    open_file = open("stored_news.pkl", "wb")
    pickle.dump(News, open_file)
    open_file.close()
        
    
  

    #return News

update_news()
