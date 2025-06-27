# Q.1 write a program to print multiplication table of a given number using for lopp

print("Welcome to the Multiplication Table Program!")
num = int(input("Enter a number to print its multiplication table:"))
for i in range  (1, 11):
    table = num * i
    print(f"{num} * {i} = {table}")

# Q.2 Write a program to greet all the person names stored in a list and which starts with 'S'

l = ['Sam', 'John', 'Sally', 'Mike', 'Sara', 'Tom']
for name in l:
    if name.startswith('S'):
        print(f"Hello {name}, welcome to the program!")
    else:
        print(f"Hello {name}, you are not in the special list.")

# Q.3 attemp Q.1 using while loop

print("Welcome to the Multiplication Table Program!")
num = int(input("Enter a number to print its multiplication table :"))
i = 1
while i <= 10:
    table = num * i
    print(f"{num}*{i} = {table}")
    i = i + 1

# Q.4 write a program to find whether a given number is prime or not

num = int(input("Enter a number to check if it is prime or not :"))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number.")

# Q.5 write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter a number to find the sum of first n natural numbers: "))

sum_n = 0
i = 1
while i <= n:
    sum_n = sum_n + i
    i = i + 1
print(f"The sum of first {n} natural numbers is: {sum_n}")