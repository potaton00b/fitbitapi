import requests
from pprint import pprint
import json
import time
import oauth2 as oauth2
import fitbit


access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzk0SjYiLCJzdWIiOiJCOTkyUEoiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNzAyMTcxMDQzLCJpYXQiOjE2NzA2MzUwNDN9.lezUzBNMtFqoSjTLTZ1CnwjkABhVshZVpxXZYLgs7TQ"
user_id = "B992PJ"
CLIENT_SECRET = "2e34bed1c540d0a5101f4f102cd59636"
header = {'Authorization' : 'Bearer {}'.format(access_token)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

print(response['user'])

for k,v in response['user'].items():
    print(k)
    print(v)
    print("\n")


steps_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/steps/date/today/today.json', headers={'Authorization': 'Bearer' + access_token})
print(steps_request.status_code)
pprint(steps_request.json()['activities-steps'])
