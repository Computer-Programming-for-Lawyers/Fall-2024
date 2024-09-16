# Initialize an empty list to fill from user input
nouns = []

# Loop to fill list with user input
noun = input("Enter a singular noun: ")
while noun != "":
    nouns.append(noun)
    noun = input("Enter a singular noun: ")

# Convert the nouns in the list to plural, printing out the results
i = 0

while i < len(nouns):
    print (nouns[i] + "s")
    i = i + 1

