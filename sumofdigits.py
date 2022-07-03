number = int(input())
evens = 0
odds = 0
while number:
    if (number % 10) % 2:
        odds += number % 10
    else:
        evens += number % 10
    number //= 10
print(f"Sum of all odd digits is {odds}")
print(f"Sum of all even digits is {evens}")
