import pyjokes

print("Here's a joke for you:")
joke = pyjokes.get_joke(category='chuck', language='en')
print(joke)