import urllib.request as urllib2

def download_file(url, file_name):
    try:
        file = urllib2.urlopen(url)
        with open(file_name, 'wb') as output:
            output.write(file.read())
        return True
    except:
        return False
     
if __name__ == '__main__':

    file = "time_series_19-covid-Confirmed.csv"
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    if download_file(url,file):
        print(f'Téléchargement du fichier {file} terminé avec succès')
    else:
        print(f'Téléchargement du fichier {file} impossible')
