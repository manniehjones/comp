"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730569742"

user_name: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
searching: str = print("Searching for", character, "in", user_name)
if "{character}, is in {user_name}":
    print (character, "found at index", user_name.find(character))
print: ("Searching for", character, "in", user_name)
if "{character}, is not in {user_name}":
    print: str = print("No instances of", character, "found in", user_name, )
