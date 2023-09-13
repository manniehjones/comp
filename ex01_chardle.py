"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730569742"

user_name: str = input("Enter a 5-character word:")
character: str= input("Enter a single character:")
print ("Searching for", character, "in", user_name)
if "{character}, is in {user_name}":
    print (character, "found at index", user_name.find(character))
count: str = str(user_name.count(character))
print (count, "instance of", character, "found in", user_name)
if exit (user_name.find(character) !=5):
    print ("Error: Word must contain 5 characters.")



