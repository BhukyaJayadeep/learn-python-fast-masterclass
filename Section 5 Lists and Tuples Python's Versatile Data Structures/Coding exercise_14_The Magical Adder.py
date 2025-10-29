# The Magical Adder
# For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
#
# The user input is of the form:
#
# a,b,c
#
# where a, b and c are numbers.
#
# Note that you do not have access to the keyboard on the remote server that will be running your code. As a result, you can't use the Run code button to execute the code. Use the Run tests button to execute your code with our test values (which are 7, 5, -1 and should return the answer 13).
#
# Your program should calculate and display the result of the calculation:
#
# a + b - c
#
# Display the result only, don't include any extra text.
#
# Examples:
#
# 1. > Please enter three numbers, separated by commas: 10,11,10
#
# Output: 11
#
# 2. > Please enter three numbers, separated by commas: 7,5,-1
#
# Output: 13

a = 10,11,10
a = input()
problem_list = a.split(",")
new_list = []
for value in problem_list:
    new_list.append(int(value))
sum = new_list[0]+new_list[1]-new_list[2]
print(sum)