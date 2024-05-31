import json
from pathlib import Path
from List import UserList

## file path
root = Path(__file__).parents[1]

PATH_FOLLOWERS = root / 'rawdata/followers_1.json'
PATH_FOLLOWING = root / 'rawdata/following.json'

def get_user(user):
    username = user['string_list_data'][0]['value']
    url = user['string_list_data'][0]['href']
    timestamp = user['string_list_data'][0]['timestamp']
            
    key = f'{username}'
    value = {'url':url, 'timestamp':timestamp, 'tags':'unsorted'}
    return key, value

user = {'title': '', 'media_list_data': [], 'string_list_data': [{'href': 'https://www.instagram.com/theguitarfreak_', 'value': 'theguitarfreak_', 'timestamp': 1716430377}]}
print(get_user(user))

## convert JSON to python data

with open(PATH_FOLLOWERS, 'r') as f_followers:
    data_followers = json.load(f_followers)
    dict_followers = {}
    for user in data_followers:
        tup = get_user(user)

with open(PATH_FOLLOWING, 'r') as f_following:
    data_following = json.load(f_following)
    data_following = data_following['relationships_following']

print(data_following)

followers = UserList(data_followers)
following = UserList(data_following)