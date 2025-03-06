# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
# ASk for user input
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second: "))
# Do a modulus division
    result = num1 % num2
# print the results
    print(f"The remainder is {result}")
    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")