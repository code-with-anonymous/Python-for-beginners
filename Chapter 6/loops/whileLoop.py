n = int(input("Enter the number: "))
product = 1
i = 1
while i <= n:
    product *= i
    i += 1

print(f"The factorial of {n} is {product}")
