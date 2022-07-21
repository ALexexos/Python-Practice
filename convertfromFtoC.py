tf = int(input("Enter current temperature in farenheit: "))
tc = (tf - 32) * 5/9
if tc < - 10:
    print("Extreme cold")
elif - 10 <= tc <= 0:
    print("Cold")
elif 0 < tc <= 10:
    print("Cool")
elif 10 < tc <= 20:
    print("Warm")
elif 20 < tc <= 30:
    print("Hot")
else:
    print("Extreme hot")
print(f"temperature in celcious: {tc:.1f}")
