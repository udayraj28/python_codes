# Q.1 write a python program to create a dictionary of hindi words with values as their english translation . provide the user with an option to look it up

print("Welcome to the Hindi-English Dictionary Program!")
hindi_dict = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभकामनाएँ": "Best wishes",
    "सुप्रभात": "Good morning",
    "शुभ रात्रि": "Good night"
}
def lookup_word():
    word = input("Enter a Hindi word to look up its English translation: ")
    translation = hindi_dict.get(word)
    if translation:
        print(f"The English translation of '{word}' is: {translation}")
    else:
        print(f"Sorry, the word '{word}' is not in the dictionary.")


# Q.2 write a python program to input eight numbers from the user and display all the unique numbers(once) in a set
print("Welcome to the Unique Numbers Program!")
def unique_numbers():
    numbers = set()
    for i in range(8):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.add(num)
    print("The unique numbers entered are:", numbers)

