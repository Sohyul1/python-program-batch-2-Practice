# Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
# Ask for user inpit
while True:
    num1 = float(input("Enter a number: "))
    num2 = float(input("One more:: "))

# Determine the difference
    diff = num1 - num2
    #print the output
    print(f"The diffrence is:  {diff}")

    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")

