from timeself import timeself


def is_five_divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False


print(is_five_divisible(20))
timeself()  # Must be the last line on the script.
