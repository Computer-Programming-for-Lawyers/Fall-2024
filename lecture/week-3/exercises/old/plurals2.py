# Initialize an empty list to fill from user input
nouns = []

# Loop to fill list with user input
in_noun = input("Enter a singular noun: ")
while in_noun != "":
    in_nouns.append(in_noun)
    in_noun = input("Enter a singular noun: ")

# Convert the nouns in the list to plural, printing out the results
for noun in nouns:
    if (noun.endswith('f') or noun.endswith('fe')) and not noun.endswith('ff'):
        # Will work with leaves, wolves, lives, knives
        # Also does the right thing for cliff, staff, tariff
        # Doesn't handle exceptions like roofs
        # Also, won't handle words with another fe or f in them (e.g. covfefe!)
        print (noun.replace('fe', 'ves').replace('f', 'ves'))
    else:
        print (noun + "s")

