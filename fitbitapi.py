import fitbit

import matplotlib.pyplot as plt
# gather_keys_oauth2.py file needs to be in the same directory. 
# also needs to install cherrypy: https://pypi.org/project/CherryPy/
# pip install CherryPy
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
import pprint as pprint


# YOU NEED TO PUT IN YOUR OWN CLIENT_ID AND CLIENT_SECRET
CLIENT_ID='2394J6'
CLIENT_SECRET='2e34bed1c540d0a5101f4f102cd59636'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

oneDate = pd.datetime(year = 2022, month = 12, day = 2)
help(auth2_client.intraday_time_series)

oneDayData = auth2_client.intraday_time_series('activities/heart', base_date=oneDate, detail_level= '1sec')
print(oneDayData)


yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')
time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})

#df = pd.DataFrame(oneDayData['activities-heart-intraday']['dataset'])


# Export file to csv
#df.to_csv(filename + '.csv', index = False)
#df.to_excel(filename + '.xlsx', index = False)
