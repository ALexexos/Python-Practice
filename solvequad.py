a = int(input("Enter first koefficient: "))
b = int(input("Enter second koefficient: "))
c = int(input("Enter third koefficient: "))
D = b**2 - 4  a  c
if D > 0:
    x1 = (- b - D**0.5) / (2 * a)
    x2 = (- b + D**0.5) / (2 * a)
    print(f"First solution: {x1:.3f}")
    print(f"Second solution: {x2:.3f}")
elif D == 0:
    x = - b / (2 * a)
    print(f"Unique solution: {x:.3f}")
else:
    print("No real solutions")
    
