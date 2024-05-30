import json
from pathlib import Path
from List import UserList

## file path
root = Path(__file__).parents[1]

PATH_FOLLOWERS = root / 'rawdata/followers_1.json'
PATH_FOLLOWING = root / 'rawdata/following.json'

## convert JSON to python data

with open(PATH_FOLLOWERS, 'r') as f_followers:
    data_followers = json.load(f_followers)

with open(PATH_FOLLOWING, 'r') as f_following:
    data_following = json.load(f_following)
    data_following = data_following['relationships_following']

def __get_user(user):
            username = user['string_list_data'][0]['value']
            url = user['string_list_data'][0]['href']
            timestamp = user['string_list_data'][0]['timestamp']
            
            dict_user = {'name':username, 'url':url, 'timestamp':timestamp, 'type':0}
            return dict_user

followers = UserList(data_followers)
following = UserList(data_following)

def exportjson(list, filename):
    path = root / f'processed/{filename}.json'

    with open(path, 'w') as f:
        json.dump(list, f, indent=2)
    print(f'exported {list} to {path}')

def tag_batch(namelist, taglist):
    pass
