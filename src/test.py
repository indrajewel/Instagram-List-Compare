from loaddata import followers, following, exportjson

print(followers.getnames())

'''
for user in followers.data:
    name = user['name']
    print(name)
'''

exportjson(followers.data, 'followers')
exportjson(following.data, 'following')