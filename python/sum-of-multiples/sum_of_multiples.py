def sum_of_multiples(limit, multiples):
    multi=[]
    for num in multiples:
        multi+= [i*num for i in range(1,limit) if i*num<limit]
    return sum(set(multi))