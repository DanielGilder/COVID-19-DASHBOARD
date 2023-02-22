import pickle



test = [{'title': 'lEspinoza: Christmas, elections and Omicron - Yahoo Philippines News', 'description': 'Our Christmas celebration this year will never be the same as it used to be before this deadly new coronavirus (Covid-19) arrived on our shores. The virus...', 'read': False},{'title': 'EU health bodies approve combined use of different Covid vaccines - pna.gov.ph', 'description': 'BRUSSELS &ndash; European Union health agencies approved on Tuesday the mixing of traditional and mRNA-based coronavirus disease 2019 (Covid-19) vaccines.&nbsp;"The combination of viral vector vaccines and mRNA vaccines produces good levels of antibodies agai…', 'read': False}]
open_file = open("stored_news.pkl", "wb")
pickle.dump(test, open_file)
open_file.close()

open_file = open("stored_news.pkl", "rb")
load = pickle.load(open_file)
open_file.close()
