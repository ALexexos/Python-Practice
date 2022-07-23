number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is complex")
else:
    for divisor in range(3, int(number**.5) + 1, 2):
        if number % divisor == 0:
            print(f"{number} is complex")
            break
    else:
        print(f"{number} is prime")
