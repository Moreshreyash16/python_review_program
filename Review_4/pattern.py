'''
@Author: Shreyash More

@Date: 2023-07-01 12:07:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-07-01 12:07:30

@Title : Hour glass Pattern
'''
rows=int(input("Enter a number "))
for i in range(0,rows):
    for j in range(rows-i,rows+1):
        print(end=" ")
    for k in range(rows-i,0,-1):
        print("*",end=" ")
    print()
for i in range(0,rows):
    for j in range(0,rows-i):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()





