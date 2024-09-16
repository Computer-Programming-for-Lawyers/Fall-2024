# justices.py

# Demo code for week 3 lecture demonstrating for-loops, lists, and split, replace, and join.

# Getting acquainted with the data and printing some information from fields.

rows = open('justices.csv').read().split('\n')

for row in rows:
    if row == '':
        continue
    fields = row.split(';')
    full_name = fields[0]
    #print(full_name)

    # Now, just print the last names only
    name_parts = full_name.split(', ')
    last_name = name_parts[0]
    first_name = name_parts[1]

    print (last_name)
