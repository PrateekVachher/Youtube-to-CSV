import pickle,csv
from scrape_data import get_data

get_data()

file_open_1 = open('datafiles/AA_SPEAKER.dat','rb')
data_1 = pickle.load(file_open_1)

csv_open = csv.writer(open('result.csv','w'))

csv_open.writerow(['Type','DateTime','Title','Channel','Description'])

for x in data_1['items']:
    csv_open.writerow(['AA_SPEAKER',x['snippet']['publishedAt'],x['snippet']['title'],x['snippet']['channelTitle'],x['snippet']['description']])

file_open_2 = open('datafiles/NA_SPEAKER.dat','rb')
data_2 = pickle.load(file_open_2)

for x in data_2['items']:
    csv_open.writerow(['NA_SPEAKER',x['snippet']['publishedAt'],x['snippet']['title'],x['snippet']['channelTitle'],x['snippet']['description']])

print('\nResults Generated in result.csv')