"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730569742"

# labels
wordz = input("Enter a 5-character word: ")
characterz = input("Enter a single character: ")

#errors
if len(wordz) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
else: 
    if len(characterz) != 1:
        print("Error: Character must be a single character.")
        exit()
    else: 
        print("Searching for {characterz} in {wordz}")

# indexes
count = 0

if wordz[0] == characterz:
    print("{characterz} found at index 0")
    count += 1
if wordz[1] == characterz:
    print("{characterz} found at index 1")
    count += 1
if wordz[2] == characterz:
    print("{characterz} found at index 2")
    count += 1
if wordz[3] == characterz:
    print("{characterz} found at index 3")
    count += 1
if wordz[4] == characterz:
    print("{characterz} found at index 4")
    count += 1

# instances
if count == 0:
    print("No instances of {characterz} found in {wordz}")
else:
    print("{count} instance{'s' if count != 1 else''} of {characterz} found in {wordz}")