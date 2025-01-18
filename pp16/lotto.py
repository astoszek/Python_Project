from random import sample


def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    return lucky_numbers
    # (może też być tak) return sample([i for i in range(1, 50)], 6
    # return sample(range(1, 50), 6)


def get_user_numbers():
    n = 6
    counter = 1
    user_numbers = []
    while counter <= n:
        try:
            number = int(input("Podaj {} liczbę (1-49): ".format(counter)))
            if number in user_numbers:
                print("Podałeś już tą liczbę! Podaj inną liczbę!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziało 1-49!")
                continue
        except ValueError:
            print("To nie jest liczba")
            continue
        user_numbers.append(number)
        counter += 1
    user_numbers.sort()
    return user_numbers


def check_user_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter


if __name__ == '__main__':
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_user_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)
