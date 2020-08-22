import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
#%%

url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
req=urllib.request.urlopen(url)
article=req.read().decode()
with open('localfile.html', 'w') as fo:
    fo.write(article)
article

article=open('localfile.html').read()
soup=BeautifulSoup(article,'html.parser')
tables=soup.find_all('table',class_='sortable')
tables

#%%
results_table=[]
for tr in tables:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td]
    results_table.append(row)
results_table=pd.DataFrame(np.array(results_table[0]).reshape((-1,3)))
results_table.columns=['PostalCode','Borough','Neighborhood']
results_table=results_table[results_table['Borough']!='Not assigned'].reset_index(drop=True)

#%%
results_table.shape

#%% get geo information
!wget -q -O 'geo.csv' https://cocl.us/Geospatial_data
#%%


















