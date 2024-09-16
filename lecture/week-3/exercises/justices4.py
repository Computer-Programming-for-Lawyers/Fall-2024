# justices4.py

# Demo code for week 3 lecture demonstrating for-loops, lists, and split, replace, and join.

# v4 given a date, return the composition of the court on that date
# Point is to show how to use boolean flags, continue, and break

search_year = int(input("Year: "))

rows = open('justices-cleaned.csv').read().split('\n')

count = 0

chiefs = True
print("Chief Justice:")

for row in rows:    
    if row == '':
        continue

    fields = row.split(';')

    title = fields[-1]

    if chiefs and title == "Associate Justice":
        print()
        print ("Associate Justices")
        chiefs = False
    
    full_name = fields[0]
    start_date = fields[3]
    end_date = fields[4]
    #print(full_name)

    # Since we care only about year, just do a simple split().
    # Also helps us deal with the (a), (b), (c) messiness
    # This will throw an error, because the original data for Harlan is missing a comma!
    # Brandeis is missing a space after a comma!
    # Clean and redo.
    start_date_parts = start_date.split(', ')
    start_year = int(start_date_parts[1])

    # For end year, sitting justices have none, so assume 2023
    if end_date == '':
        end_year = 2023
    else:
        end_date_parts = end_date.split(', ')
        end_year = int(end_date_parts[1])

        
    if not chiefs and start_year > search_year:
        print(f"Breaking on {full_name}")
        break
    elif search_year >= start_year and search_year <= end_year:
        print(f'{full_name} {start_date} - {end_date}')
        count += 1

if count > 9:
    print()
    print("Too many justices: someone new was named this year!")
elif count < 9:
    print()
    print("Not enough justices. Vacancy trouble this year?")
