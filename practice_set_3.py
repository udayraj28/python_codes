# Q1. write a python program to display user entered name followed by good morning using the input function

print("Welcome to the Greeting Program!")
name = input("Enter your name :")
print("Good morning", name + "!\nHow are you today?")

# Q2. Write a python program to fill in a letter template given below with name and date entered by the user

print("Welcome to the Letter Template Program!")
name = input("Enter your name: ")
date = input("Enter the date (DD/MM/YYYY): ")

Letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

Letter = Letter.replace("<|Name|>", name).replace("<|Date|>", date)
print(Letter)

# Q3. Write a python program to detect double spaces in a string entered by the user and replace them with single space

print("Welcome to the Double Space Detection Program!")
string = input("Enter a string with possible double spaces: ")
index = string.find("  ")
if index != -1:
    print("Double spaces detected at index:", index)
string = string.replace("  ", " ")
print("String after replacing double spaces with single space:", string)

# Q4. Write a python program to format the following string using the escape sequence characters

print("Welcome to the String Formatting Program!")
formatted_string = "Hello, \"Python\"! \n\tWelcome to the world of programming.\nLet's learn and grow together!"
print(formatted_string)