import random

def random_gen():
    while True:
        random_number = random.randint(10, 20)
        yield random_number
        if random_number == 15:
            break

# Example usage:
gen = random_gen()
for number in gen:
    print(number)
