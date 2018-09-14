import random

def generate_random_list():
    # Generate Random List
    random_list = random.sample(range(45), 34)
    print("Random List is - {0}".format(random_list))
    return random_list 

def sort_list(rlist):
    # Sorting - Insert Sort
    for i in range(1, len(rlist)):
        key = rlist[i] 
        position = i 
        while position > 0 and rlist[position -1] > key: 
            rlist[position] = rlist[position-1]
            rlist[position - 1] = key
            position = position - 1
        rlist[position] = key
    print("Sorted List is - {0}".format(rlist))
    return rlist


def binary_search(rlist, fval):
    # Binary Search
    while len(rlist) is not 1:
        rlist_len = len(rlist)
        f_ele = rlist[:round(len(rlist)/2)]
        s_ele = rlist[round(len(rlist)/2):]
        if f_ele[-1] >= fval:
            rlist = f_ele
            continue
        elif s_ele[-1] >= fval:
            rlist = s_ele
            continue
        else: 
            print("{0} value does not exists".format(fval))
            return False
        print(rlist[0])
    
    if  rlist[0] is fval:
        print("{0} value exists".format(fval))
        return True
    else: 
        print("{0} value does not exists".format(fval))
        return False

rlist = generate_random_list()
sorted_rlist = sort_list(rlist)
search_val = int(input("Enter the search value: "))
binary_search(sorted_rlist, search_val)
