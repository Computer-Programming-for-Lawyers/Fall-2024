# justices.py

# Demo code for week 3 lecture demonstrating for-loops, lists, and split, replace, and join.

# v2: What are the terms for each justice?
# Don't mess with months or days. Just years.

#rows = open('justices.csv').read().split('\n')
rows = open('justices-cleaned.csv').read().split('\n')

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

    # Will choke on asterisks, so remove those
    term_years = int(end_year) - int(start_year)

    print(f"{full_name}: {start_year} - {end_year} ({term_years} years)")
