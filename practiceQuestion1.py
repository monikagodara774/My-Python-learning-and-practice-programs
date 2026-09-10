#take two numbers as input from user.print their sum, difference, product, and remainder

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a % b)

#take a number as a input.print whether it is even or odd using % operator and comparison operator
# a = int(input("enter the any number: "))
# print(a % 2 == 0,"number is even" )
# print(a % 2 == 1,"number is odd")

#take the user age as input.check and print whether they are eligible to vote(age >= 18) and whether they are a senior citizen(age >= 60).print both result
# age = int(input("Enter the your age"))
# print(age >= 18, "They are eligible to vote")
# print(age >= 60, "They are senior citizen")

#A student scored marks in 3 subjects.Take all three as input, calculate the total and average, and print both using an f-string
chemistry = int(input("Enter the chemistry marks"))
physics = int(input(("Enter the physics marks")))
math = int(input("Enter the math marks"))
total = chemistry + physics + math
average = total/3
print(f"This is the total = {total} and This is the average = {average} of three subjects")