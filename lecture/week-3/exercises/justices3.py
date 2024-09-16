# justices.py

# Demo code for week 3 lecture demonstrating for-loops, lists, and split, replace, and join.

# v3: Who has served for more than n years? What is the average term?

min_term = int(input("Display justices who have worked at least how many years? "))

rows = open('justices-cleaned.csv').read().split('\n')

total = 0
count = 0

for row in rows:    
    if row == '':
        continue

    fields = row.split(';')
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
    start_year = start_date_parts[1]

    # For end year, sitting justices have none, so assume 2023
    if end_date == '':
        end_year = "2023"
    else:
        end_date_parts = end_date.split(', ')
        end_year = end_date_parts[1]

    term_years = int(end_year) - int(start_year)
    
    if term_years >= min_term:
        # Will choke on asterisks, so remove those
        total += term_years
        count += 1

        print(f"{full_name}: {start_year} - {end_year} ({term_years} years)")

print (f"Average term: {total / count} years")
