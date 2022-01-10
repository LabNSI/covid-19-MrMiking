import urllib.request as urllib2
import csv
from covid19v1 import *
from covid19v2 import *

def data_for_country(data, state = "", country = ""):
    for pays in data:
        if pays['Province/State'] == state and pays['Country/Region'] == country:
            return pays

if __name__ == '__main__':

  file = "time_series_covid19_confirmed_global.csv"
  url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

  if download_file(url,file):
      print(f'Téléchargement du fichier {file} terminé avec succès')
      countries = read_CSV(file)
      print("----------------------------------")
      france = data_for_country(countries, '', 'France')
      print(france)

  else:
      print(f'Téléchargement du fichier {file} impossible')
