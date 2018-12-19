# -*- coding: utf-8 -*-
"""
@author: Spikee
"""

def filled():
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==0:
                return True
        else:
            return False

def magicConstant():
    return n*((n**2+1)//2)
    
def magicSquare(matrix):
    print()
    i=n-1
    j=n//2
    value=magicConstant()

    num=(key-value)//3+1
    
    prev_j = j
    while filled():

        if i==n:
            i=0
        if i==n and j==n:
            i,j=0,0
        if j==n:
            j=0

        if matrix[i][j]:
            i=i-1
            j=prev_j

        else:
            matrix[i][j]=num
            num+=1
            prev_j=j
            j+=1
            i+=1
        
    return matrix

n=int(input("Select Value of N "))
key=int(input("Enter the Magic SUM "))
matrix=[[0 for i in range(n)]for j in range(n)]
magic=magicSquare(matrix)

print("MAGIC SQUARE OF",n,"*",n)
for i in range(n):
    for j in range(n):
        print(magic[i][j],end=" ")
    print()