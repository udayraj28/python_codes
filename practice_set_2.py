# Q.1 Write a python program to add two numbers

print("Welcome to the Addition Program!")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

result = num1 + num2
print("Addition of two numbers is :", result)


# Q.2 Write a python program to find the remainder when a number is divided by z

print("Welcome to the Remainder Program!")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

print("Remainder when first number is divided by second number is :", num1 % num2)


# Q.3 Check the type of the variable assigned using the input function

print("Welcome to the Type Check Program!")
num = int(input("Enter a number: "))  #int before input will convert the string into an integer type
print("The type of the variable is:", type(num))

# If you want to keep the input as a string, you can use:
num = (input("Enter a number: "))
print("The type of the variable is:", type(num))


# Q.4 Use comparison operator to find out whether the given variable a is greater than b

print("Welcome to the Comparison Program!")
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
if a > b:
    print("a is greater than b")

elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")


# Q.5 Write a python program to find out the average of given numbers entered by the user

print("Welcome to the Average Calculation Program!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("The average of the two numbers is:", (num1 + num2) / 2)


# Q.6 Write a python program to calculate the square of a number entered by the user

print("Welcome to the Square Calculation Program!")
num = float(input("Enter a number to find its square: "))
print("The square of the number is:", num ** 2)