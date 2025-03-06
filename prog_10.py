# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# Ask for user input
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second: "))
# Get the numbers between
    start = int(min(num1, num2))
    end = int(max(num1, num2))
    for i in range (start + 1, end ):
       # Print the output
        print(i)
    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")
