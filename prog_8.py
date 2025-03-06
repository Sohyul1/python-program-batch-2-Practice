# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
# Make an empty list
empt_list = []
num = 0

# Make the while loop
while num <= 100:
   # Filter out the odd nmber
    if num % 2 != 0:
        empt_list.append(num)
    num += 1

# Print all odd numbers
print(f"The odd numbers from 0 to 100 are:\n\n{empt_list}")
