# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:34:31 2017

@author: Bruce
"""
import random

class Matrix:
    
    def __init__(self, mat=None, rowNum=0, colNum=0):
        if rowNum and colNum:
            self.rowNum = rowNum
            self.colNum = colNum
            self.array = [[random.randint(-5, 5) for j in range(self.colNum)] for i in range(self.rowNum)]
            self.dim = (self.rowNum, self.colNum)
        elif mat and type(mat) == list:
            self.array = mat
            self.rowNum = len(self.array)
            self.colNum = len(self.array[0])
            self.dim = (self.rowNum, self.colNum)
        else:
            raise TypeError('Invalid entry! Provide your own matrix in the form of a list of lists, or enter how many rows and \
                  columns you want for a randomly generated matrix.')

    def height(self):
        return self.rowNum
    def width(self):
        return self.colNum
    def getDim(self):
        print("{} rows by {} columns".format(self.rowNum, self.colNum))
        
    def __getitem__(self, ele):
        (i, j) = ele
        print (self.array[i][j])
    def __setitem__(self, ele, new_value):
        self.new_value = new_value
        (i, j) = ele
        self.array[i][j] = new_value
        return self.array
    
    def __str__(self):
        return '\n'.join([''.join(['{:5}'.format(value) for value in row]) for row in self.array])
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.dim != other.dim:
                raise ValueError('Matrices do not have same dimensions!')
            else:
                self.newArray=[]
                for i in range(self.rowNum):
                    row=[]
                    for j in range(self.colNum):
                        row.append(self.array[i][j] + other.array[i][j])
                    self.newArray.append(row)
                return Matrix(self.newArray)
        else:
            raise TypeError('Inputs must be either class: Matrix or integer!')
        
    def __pow__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            self.newArray=[]
            for i in range(self.rowNum):
                row=[]
                for j in range(self.colNum):
                    row.append(self.array[i][j] ** other)
                self.newArray.append(row)
            return Matrix(self.newArray)
    
    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            self.newArray=[]
            for i in range(self.rowNum):
                row=[]
                for j in range(self.colNum):
                    row.append(self.array[i][j] * other)
                self.newArray.append(row)
            return Matrix(self.newArray)
        elif isinstance(other, Matrix):
            if (self.colNum) != other.rowNum:
                raise ValueError('Column length of matrix A does not match,\
                                 the row height of matrix B')
            newArray=[]
            for i in range(self.rowNum):
                row=[]
                for j in range(other.colNum):
                    col=[]
                    for k in range(other.rowNum):
                        col.append(self.array[i][k] * other.array[k][j])
                    row.append(sum(col))
                newArray.append(row)
            return Matrix(newArray)
    
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.dim != other.dim:
                raise ValueError('Matrices do not have same dimensions!')
            else:
                self.newArray=[]
                for i in range(self.rowNum):
                    row=[]
                    for j in range(self.colNum):
                        row.append(self.array[i][j] - other.array[i][j])
                    self.newArray.append(row)
                return Matrix(self.newArray)
        else:
            raise TypeError('Inputs must be either class: Matrix or integer!')
            
    def __eq__(self, other):
        print (self.array == other.array)
            
    def __pos__(self):
        return Matrix(self.array)
    def __neg__(self):
        return Matrix(self.array) * -1

#Need scalar * Matrix
#Need ** operator

m1 = Matrix([[2, 5, -3], [1, 0, -4]])
m2 = Matrix(rowNum=2, colNum=3)

print('Matrix 1 \n'+ str(m1)+"\n")
print('Matrix 2 \n'+ str(m2)+"\n")


print('Matrix 3 \n'+ str(m3)+"\n")

m1==m3