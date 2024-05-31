import datetime

def names_only(data1, data2):
    # data1 = followers data2 = following
    list1 = [x['name'] for x in data1]
    list2 = [x['name'] for x in data2]
    return list1, list2

def not_in(list1, list2):
    difference1 = [x for x in list1 if x not in list2]
    difference2 = [x for x in list2 if x not in list1]
    max = 0
    if len(difference1) >= len(difference2):
        max = len(difference1)
    else: 
        max = len(difference2)
    return difference1, difference2, max

def print_diff(diff1, diff2, max):
    print('NOT FOLLOWING')
    for x in diff1:
        print(x)
    print(f'''


''')
    print('NOT FOLLOWED BY')
    for x in diff2:
        print(x)

    
    # print('NOT IN LIST 1             |      NOT IN LIST 2')
    # for x in range(max):
    #     print(f'''{diff1[x]:<25} |      {diff2[x]:<25}''')
    
    return diff1, diff2