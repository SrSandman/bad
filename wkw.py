import random

def lottery():

    for i in range(10):
        yield random.randint(1, 40)


    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
