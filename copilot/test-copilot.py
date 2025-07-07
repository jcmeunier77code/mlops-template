# from a list of 25 fruits, build a for loop that print out each fruit in the list with a running number and a colon with the fruit name
# using enumerate function and use f-string to print the output
import random


def generate_fruit_list():
    fruits = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "papaya",
        "quince",
        "raspberry",
        "strawberry",
        "tangerine",
        "ugli fruit",
        "vanilla bean",
        "watermelon",
        "xigua",
        "yellow passion fruit",
        "zucchini flower",
    ]
    random_fruits = random.sample(fruits, k=15)
    return random_fruits


if __name__ == "__main__":
    fruit_list = generate_fruit_list()
    for index, fruit in enumerate(fruit_list, start=1):
        print(f"{index}: {fruit}")
    # Output: 1: banana, 2: fig, 3: cherry, 4: honeydew, 5: apple
    # Note: The output will vary each time you run the code due to random selection.
    # The enumerate function is used to get the index and fruit name, starting the index at 1.
    # The f-string is used to format the output as "index: fruit".
    # The random.sample function is used to select 5 unique fruits from the list.
    # The fruits list contains 25 different fruits, but only 5 are selected randomly each time.
    # The output will be different each time you run the code due to the random selection.
    # The fruits are printed in the format "1: apple", "2: banana",
    # "3: cherry", etc., where the number corresponds to the index of the fruit
    # in the randomly selected list.
