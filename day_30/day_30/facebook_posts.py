facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError as message:
            print(f"Sorry! It seems that this key, {message}, does not exist")
        else:
            total_likes += post.get("Likes", 0)
    
    return total_likes


#count_likes(facebook_posts)

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        return fruit + " pie"
    except IndexError as message:
        output = "Fruit" + " pie"
        print (output)

make_pie(3)

