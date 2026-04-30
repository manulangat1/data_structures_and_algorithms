import random
import string

print("".join(random.choices(string.ascii_letters, k=5)))


def random_spacing():
    for _ in range(random.randrange(1, 5)):

        print()
