import random
import time


def random_wait():
    wait_time = random.uniform(1, 5)
    time.sleep(wait_time)


def process_user(user):
    start_time = time.time()
    random_wait()
    print(f"User: {user} was processed...")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for processing user: {user} was: {execution_time}")


def sum_numbers_from_string(string):
    numbers = []
    for each_character in string:
        if each_character.isdigit():
            numbers.append(int(each_character))
    total = 0
    for each_number in numbers:
        total = total + each_number

    return total
