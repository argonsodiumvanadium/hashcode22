from sys import argv

def get_pizza(filename):
    with open(filename) as f:
        data = f.read().split(' ')
        return {
                'ingredients' : data[1:],
            }

def compare_pizza(pizza, fname):
    with open(fname) as f:
        likes = f.read().split('\n')[1::2]
        dislikes = f.read().split('\n')[::2][1:]

        return compare_likes(pizza,likes,dislikes)

def compare_likes (pizza, likes,dislikes):
    counter = 0
    pizzaset = set(pizza['ingredients'])

    for like,dislike in zip(likes,dislikes):
        likeset = set(like.split(' ')[1:])
        dislikeset = set(dislike.split(' ')[1:])

        if len(likeset & pizzaset) != 0 and len(dislikeset & pizzaset) == 0:
            counter += 1

    return counter

def main():
    pizza = get_pizza(argv[1])
    print(compare_pizza(pizza, argv[2]))

if len(argv) == 1:
    print('python3 tester.py [ ideal pizza file ] [ input file ]')
else:
    main()
