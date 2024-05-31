from functions import *
from loaddata import followers, following

names = names_only(followers.data, following.data)
diff = not_in(names[0], names[1])
print_diff(diff[0], diff[1], diff[2])

