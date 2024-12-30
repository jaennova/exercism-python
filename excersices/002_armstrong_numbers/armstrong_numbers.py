def is_armstrong_number(number):
    size = len(str(number))
    sum_of_powers = 0
    for i in str(number):
        sum_of_powers += int(i) ** size

    return sum_of_powers == number
