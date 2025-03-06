# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# MAke an empty list
emp_list = []
# ASk for user input
while True:
    emp_list.clear()  
    for i in range(1,11):
        ans = float(input(f"Enter number {i}: "))
        emp_list.append(ans)
# gget the difference
    total = sum(emp_list[1:])
    diff = emp_list[0] - total 
# print the result
    print(f"The result is: {diff}")
    ans = input("Repeat?(y/n): ").lower()
    if ans == "n":
        print("Good Bye!")

