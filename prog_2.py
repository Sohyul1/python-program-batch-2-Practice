# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
# Ask for ussr input 
while True:
    num1 = float(input("Enter a number: "))
    num2 = float(input("One more:: "))

# Determine if the numbers are equal or not
    if num1 != num2:
        print("Not Equal")
    else:
        print(" ")

    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")
# PRint the output