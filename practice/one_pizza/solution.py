from sys import argv
from .tester import compare_pizza

# too lazy to complete

def main():
    ingred_holder = get_like_dislike_counters(argv[1])
    pizza = generate_pizza(ingred_holder,5)

# add a system to count the 
def get_like_dislike_counters(fname):
    ingred_holder = {}
    with open(fname) as f:
        data = f.read().split('\n')
        likes_of_users    = data[1::2]
        dislikes_of_users = data[::2][1:]

        for likes,dislikes in zip(likes_of_users, dislikes_of_users):
            ingred_holder = update_like_holder(like_holder,likes,dislikes)
    
    return ingred_holder

def update_like_holder (lh, likes, dislikes):
    for like in likes.split(' ')[1:]:
        if like not in lh:
            lh[like] = 0
        lh[like] += 1
    for dislike in dislikes.split(' ')[1:]:
        if dislike not in lh:
            lh[dislike] = 0
        lh[dislike] -= 1
    return lh

def generate_pizza(ingred_holder,num):
    arr = [''] * num

    for key in ingred_holder

if len(argv) != 2:
    print ('python3 solution.py [ users ] [ output file  ]')
else:
    main()
