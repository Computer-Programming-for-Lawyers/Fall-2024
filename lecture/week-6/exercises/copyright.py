### copyright.py
# New for 2023
# Given sample solution code for copyright.py in week 2
# Show how functions can make the code simpler and more streamlined

# The sample code is one way to solve this problem.
# It is ripe for streamlining through functions.

# Must select a good default value.
while True:

    # Date of publication.
    year = int(input("In what year was the work published? "))
    while year < 1923:
        print("The year input must be a number greater than 1922.")
        year = int(input("In what year was the work published? "))

    month = int(input("In what month was the work published? "))
    while month > 12 or month < 1:
        print("The month input must be a number between 1 and 12.")
        month = int(input("In what month was the work published? "))

    day = int(input("On what day of the month was the work published? "))
    while day > 31 or day < 1:
        print("The day input must be a number between 1 and 31.")
        day = int(input("On what day of the month was the work published? "))

    # Other questions.
    notice_in  = input("Was notice of copyright given? ")
    renewed_in = input("Was the work properly renewed (manually or automatically)? ")
    expired_in = input("Has the original term of copyright protection expired? ")

    noticed = notice_in == 'y' or notice_in == 'yes'
    renewed = renewed_in == 'y' or renewed_in == 'yes'
    expired = expired_in == 'y' or expired_in == 'yes'

    # Execute the flowchart.
    if year >= 2003:
        if not expired:
            print('In Copyright')
        else:
            print('In Public Domain')

    elif year >= 1989 and month >= 3:
        print('In Copyright')

    elif year >= 1978:
        if noticed:
            print('In Copyright')
        else:
            print('In Public Domain')

    elif year >= 1964:
        if expired or not noticed:
            print('In Public Domain')
        else:
            print('In Copyright')

    else:
        if expired or not renewed or not noticed:
            print('In Public Domain')
        else:
            print('In Copyright')

    print()
    go_again = input("Do you want to analyze another work? ")
    if not (go_again == "Yes" or go_again == "yes" or go_again == "y"):
        break
    
print("Goodbye!")
