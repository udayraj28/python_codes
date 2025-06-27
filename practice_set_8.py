# Q.1 Write a python program using function to find the greatest of three numbers.

def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

G = greatest(a, b, c)
print(f"The greatest of the three numbers {a}, {b}, and {c} is: {G}")

# Q.2 Write a python program using function to convert temperature from celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Q.3 Write a python program recursive function to print the sum of first n natural numbers.

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

n = int(input("Enter a number to find the sum of first n natural numbers: "))
result = sum(n)
print(f"The sum of first {n} natural numbers is: {result}")

# Q.4 Write a python program using function to print first n lines of the following pattern:  
# ***
# **
# *

def pattern(n):
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input("Enter the number of lines for the pattern: "))
pattern(n)

# Q.5 Write a python program using function to covert inch into cm

def inch_to_cm(n):
    cm = n * 2.54
    return cm

n = int(input("Enter the number to covert into cm:"))

x = inch_to_cm(n)
print(f"The {n} inch in cm is: {x}")

# Q.6 Write a python program using function to remove a given word from a list ad strip it at the same time.

def remove_and_strip_word(word_list, word_to_remove):
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

word_list = ['  apple ', 'banana', '  cherry  ', 'apple', '  date']
word_to_remove = 'apple'
result = remove_and_strip_word(word_list, word_to_remove)
print("Original list:", result)