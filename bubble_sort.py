import random

def generate_random_list():
    # Generate Random List
    random_list = random.sample(range(35), 35)
    print("Random List is - {0}".format(random_list))
    return random_list 

def bubble_sort(rlist):
    # bubble sort
    rlist = rlist
    for i in range(len(rlist)):
        for j in range(len(rlist)-1):
            if rlist[j] > rlist[j+1]:
                key = rlist[j]
                rlist[j] = rlist[j+1]
                rlist[j+1] = key
    print("Bubble Sorted List - {0}".format(rlist))

rlist = generate_random_list()
bubble_sort(rlist)
