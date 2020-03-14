def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []
    for i in lists: new_list += i
    return(new_list)
  

def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    if list!=[]: return list.index(list[-1]) + 1 
    else: return 0
    

def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    result = initial
    for l in list:
        result = function(result, l)
    return result


def foldr(function, list, initial):
    result = initial
    for l in reverse(list):
        result = function(l, result)
    return result


def reverse(list):
    return list[::-1]
