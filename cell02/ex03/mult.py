num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
print(f"{num1} * {num2} = {num1 * num2}")
if num1 * num2 > 0:
    print("The resuit is positive.")
elif num1 * num2 < 0:
    print("The result is negative.")
else:
    print("the result is positive and negative.")
