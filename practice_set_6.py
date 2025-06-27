# Q.1 Write a python program to find the greatest of four numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("The greatest number is: ",a)
elif b >= a and b >= c and b >= d:
    print("The greatest number is: ",b)
elif c >= a and c >= b and c >= d:
    print("The greatest number is: ",c)
else:
    print("The greatest number is: ",d)

# Q.2 Write a python program to find out whether a student is pass or fail if it requires total 40% and atleast 33% in each subject to pass. Take three subjects marks as input from the user.

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

total_marks = sub1 + sub2 + sub3
if total_marks >= 120 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("The student is pass.")
else:
    print("The student is fail.")

# Q.3 A spam comment is defined as a comment that contains the words "make a lot of money", "buy now", "click this", "subscribe this", "click here". Write a python program to detect whether a comment is spam or not.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"

message = input("Enter your comment: ")

if( p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is spam.")
else:
    print("This comment is not spam.")

# Q.4 Write a python program to find out whether a given username contains less than 10 characters or not.\

username = input("Enter your username: ") 
if len(username) < 10:
    print("The username is valid.")
else:
    print("The username is invalid. It should contain less than 10 characters.")

# Q.5 Write a python program to find out whether a given name is present in a list or n

names = ["uday", "sachin", "rohit", "virat", "dhoni"]
name = input("Enter a name to search: ")
if name in names:
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")

# Q.6 Write a python program to calculate the grade of a student from the marks from the following table:
# 90 - 100 = Excellent
# 80 - 90 = A
# 70 - 80 = B
# 60 - 70 = C
# 50 - 60 = D
# < 50 = Fail

marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Your grade is: Excellent")
elif marks >= 80 and marks < 90:
    print("Your grade is: A")
elif marks >= 70 and marks < 80:
    print("Your grade is: B")
elif marks >= 60 and marks < 70:
    print("Your grade is: C")
elif marks >= 50 and marks < 60:
    print("Your grade is: D")
else:
    print("You are fail.")

# Q.7 Write a python program to find out whether a given post is talking about "Python" or not.

post = input("Enter your post: ")
if "Python" in post:
    print("The post is talking about Python.")
else:
    print("The post is not talking about Python.")