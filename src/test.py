from functions import*
from loaddata import followers, following
from copy import deepcopy
#print(followers.getnames())




'''
for user in followers.data:
    name = user['name']
    print(name)
'''



# TAGS
'''
follower tags:
'personal'
'pine'
'content'
'band'
'spam'
'memes'
'local'
''
'''

'''

tags = ['band']

tag_batch(names, tags)
'''
names = following.getnames()
print(following.data)
print(names)

'''
for user in following.data:
    for name in names:
        if user['name'] == name:
            print('True')
        else:
            print('False')
'''
#print(names)

#exportjson(followers.data, 'followers')
#exportjson(following.data, 'following')