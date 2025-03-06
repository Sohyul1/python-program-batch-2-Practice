# Prog4: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
# Ask fr user input
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second: "))
# GEt the quotient
    quotient = int(num1 // num2)
# Print the output(without decimal)
    print(f"The quotient is:  {quotient}")
    
    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")