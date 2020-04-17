# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:14:24 2020

@author: Novin
"""
# program for matrix transpose 


matrix = [[1,2,3,4],[2,3,4,6],[6,7,8,9]]
rowNumber = len(matrix)
colNumber = len(matrix[0])

transpose = []
tranRowNumber = colNumber
tranColNumber = rowNumber


for i in range(tranRowNumber):
    row = []
    for j in range(tranColNumber):
       row.append(matrix[j][i])
    transpose.extend([row])

print(transpose)
print('transpose dim : row Number:',colNumber,'\t col Number:',rowNumber)


# program for adding two matrix

first = [[1,2,3,4],[2,3,4,6],[6,7,8,9]]
second = [[1,2,3,4],[2,3,4,6],[6,7,8,9]]

summation =[]
rowNumber = len(first)
colNumber = len(first[0])


for i in range(rowNumber):
    row = []
    for j in range(colNumber):
       row.append(first[i][j]+second[i][j])
    summation.extend([row])
    
    
print('the summation of two matrix is : ',summation)

