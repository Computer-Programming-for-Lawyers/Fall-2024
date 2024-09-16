# Initialize an empty list to fill from user input
nouns = []

# Loop to fill list with user input
in_noun = input("Enter a singular noun: ")
while in_noun != "":
    # TODO:
    # words that end with f or that end with fe are made plural
    # with ves
    # knife -> knives
    # calf -> calves
    # words that end ff don't get this treatment
    nouns.append(in_noun)
    in_noun = input("Enter a singular noun: ")

# Convert the nouns in the list to plural, printing out the results
for noun in nouns:
    print(f"{noun}s")
