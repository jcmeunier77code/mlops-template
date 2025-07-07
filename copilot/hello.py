# build a random list of fruit
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
    ]
    random_fruits = random.sample(fruits, k=5)
    return random_fruits


if __name__ == "__main__":
    fruit_list = generate_fruit_list()
    print("Random Fruit List:", fruit_list)
    # Output: Random Fruit List: ['banana', 'fig', 'cherry', 'honeydew', 'apple']
    # Note: The output will vary each time you run the
