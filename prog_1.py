# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
# Ask the user to input a number
while True:
    num1 = float(input("Enter a number: "))
    num2 =float(input("Enter one more :"))
# Determine the smaller number
# Print the smaller number 
    if num1 > num2:
        print(f"{num2} is the smaller number.")
    else:
        print(f"{num1} is the smaller number.")

    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")
        break

