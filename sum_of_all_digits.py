def sum_of_digits(number):
    print(f"Calculating Sum Of Digits For: {number}")
    even_sum = 0
    odd_sum = 0
    while number:
        if number % 2:
            odd_sum += number % 10
        else:
            even_sum += number % 10
        number //= 10
    print(f"Sum Of Even digits Is {even_sum}")
    print(f"Sum Of Odd digits Is {odd_sum}")
    print(f"Sum Of All Digits Is: {even_sum + odd_sum}")

from random import randint
sum_of_digits(randint(100,999))
sum_of_digits(randint(1000,9999))
sum_of_digits(randint(10000,99999))
