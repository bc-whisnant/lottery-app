import random

def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = get_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched ${}".format(matched_numbers))
    print("You won ${}".format(100 ** len(matched_numbers)))


def get_player_numbers():
    number_csv = input('Enter your six numbers separated by commas: ')
    # create set of integers based on this number_csv variable
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

def get_lottery_numbers():
    values = set()

    while len(values) < 6:
        values.add(random.randint(1, 20))

    return values

menu()