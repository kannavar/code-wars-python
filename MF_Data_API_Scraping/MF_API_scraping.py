import requests
import re
import pandas as pd

### Problem statement - Given a category of the funds give me the list of funds 
### which are outperforming in 3 year category 

def queryMFList(mf_data:"list",category):
    schemes=dict()
    for i in mf_data:
        if(category in i['schemeName']):
            schemes[i['schemeCode']]=i['schemeName']
    return schemes

def fetchMFData(mf_schemes:"dict"):
        
    for isin in mf_schemes.keys():
        mf_data = requests.get(f'https://api.mfapi.in/mf/{isin}').json()
        df = pd.DataFrame(mf_data['data'])
        df.to_csv(f"./mf_data/{isin}.csv",index=False)
    return

if __name__=='__main__':
    try:
        r = requests.get('https://api.mfapi.in/mf')
        print(r.status_code)
        all_mfs = r.json()

    except Exception as e:
        print("Error occured ",e)

    mf_filtered=queryMFList(all_mfs,'Flexi')

    fetchMFData(mf_filtered)


