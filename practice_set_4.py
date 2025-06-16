# Q.1 Write a python program to store seven fruits in a list entered by the user

print("Welcome to the Fruit List Program!")
fruits = []
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
fruit = input("Please enter the fruit name :")
fruits.append(fruit)
print("The list of fruits is:", fruits)

# Q.2 Write a python program to accept marks of 6 students and display them in a sorted manner

print("Welcome to the Marks Sorting Program!")
marks = []
mk = float(input("Please enter the marks of student 1: "))
marks.append(mk)
mk = float(input("Please enter the marks of student 2: "))
marks.append(mk)
mk = float(input("Please enter the marks of student 3: "))
marks.append(mk)
mk = float(input("Please enter the marks of student 4: "))
marks.append(mk)
mk = float(input("Please enter the marks of student 5: "))
marks.append(mk)
mk = float(input("Please enter the marks of student 6: "))
marks.append(mk)
marks.sort()
print("The sorted marks of the students are:", marks)

# Q.3 Write a python program to sum a list with 4 numbers entered by the user

print("Welcome to the List Sum Program!")
numbers = []
num = float(input("Please enter number 1: "))
numbers.append(num)
num = float(input("Please enter number 2: "))
numbers.append(num)
num = float(input("Please enter number 3: "))
numbers.append(num)
num = float(input("Please enter number 4: "))
numbers.append(num)
print("The sum of the numbers in the list is:", sum(numbers))

# Q.4 Write a python program to find the count the number of zeroes in a list of 5 numbers entered by the user

print("Welcome to the Zero Count Program!")
numbers = []
num = float(input("Please enter number 1: "))
numbers.append(num)
num = float(input("Please enter number 2: "))
numbers.append(num)
num = float(input("Please enter number 3: "))
numbers.append(num)
num = float(input("Please enter number 4: "))
numbers.append(num)
num = float(input("Please enter number 5: "))
numbers.append(num)
zero_count = numbers.count(0)
print("The count of zeroes in the list is:", zero_count)