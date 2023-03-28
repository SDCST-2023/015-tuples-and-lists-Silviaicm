#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
list = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
x=input("Pick one name from the list: ")
z=list.index(x)
list.remove(x)
y=input("Enter a replacemet: ")
list.insert(z,y)
print(list)