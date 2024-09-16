### Name: Winnona Bernsen
### Filename: coldcall.py
### Description: takes a list of students (poorly formatted, copy/pasted from Canvas)
###              and cold calls a student randomly without doxxing their full name.
### Dependencies: random library! Have to make sure the cold-call is random.
### Help: N/A

import random

#grab students.txt
filename = "students.txt"
list_students = []

i = 1
# read the raw file
rawfile = open(filename).read().split("\n")

# HOUSE METHOD: take the row in the rawfile, transform data from that row, put that data into a new list
for row in rawfile:
  #all names in this file are on every 6th row, but mileage may vary
  if i == 6:
    # separate first and last names from the full name
    (first, last) = (row.split(" ")[0], row.split(" ")[1])

    # append last initial to first name, append to a student list.
    firstname_and_initial = first + " " + last[0] + "."
    list_students.append(firstname_and_initial)
    i = 0

  i += 1

#find a random student and print their name!
cold_call = random.choice(list_students)
print(cold_call)
