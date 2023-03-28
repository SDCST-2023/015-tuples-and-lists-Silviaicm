#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""

z=input("Enter an integer")
x=input("Enter an integer")
c=input("Enter an integer")
v=input("Enter an integer")
b=input("Enter an integer")
n=input("Enter an integer")
m=input("Enter an integer")
a=input("Enter an integer")
s=input("Enter an integer")
d=input("Enter an integer")

list=[z,x,c,v,b,n,m,a,s,d]
q=max(list)
print(f"The largest number you entered is {q}")