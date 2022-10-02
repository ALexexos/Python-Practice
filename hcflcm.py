def HCF(number1, number2):
    if number1 < number2:
        number1, number2 = number2, number1
    while number2:
        number1, number2 = number2, number1 % number2
    print(number1)
    return number1

def LCM(number1, number2):
    result = number1 * number2 // HCF(number1, number2)
    print(result)
    return result

LCM(57,77)

