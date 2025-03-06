# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
# MAke an empty list
empt_list = []
# Ask for user input
while True:
    empt_list.clear()  
    for i in range(1,11):
        ans = float(input(f"Enter number {i}: "))
        # Filter out the even numbers
        if ans % 2 == 0:
            empt_list.append(ans)
            total = len(empt_list)

    # Print the output
    print(f"There are {total} even numbers. ")

    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")
