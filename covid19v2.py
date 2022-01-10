import urllib.request as urllib2
from covid19v1 import *
import csv

def read_CSV(file):
    datas = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            datas.append(row)
        return datas

if __name__ == '__main__':

    file = "time_series_covid19_confirmed_global.csv"
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
        countries = read_CSV(file)
        print("liste des pays et régions recencés")
        print("----------------------------------")
        for row in countries:
            print(row['Province/State'], row['Country/Region'])
    else:
        print(f'Téléchargement du fichier {file} impossible')

    
    




    





