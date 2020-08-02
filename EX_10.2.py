# EX_10.2:
import numpy as np
import matplotlib.pyplot as plt

vec1 = np.array([ -1., 4., -9.])
mat1 = np.array([[ 1., 3., 5.], [7., -9., 2.], [4., 6., 8. ]])
print (mat1)

#2.1;
print ('2.1: ')
vec2 = (np.pi/4) * vec1
print ('vector number 1 is equal to:\n',vec1)
print ('vector number 2 is equal to:\n',vec2, '\n')

#2.2:
print ('2.2: ')
vec3 = np.cos(vec2)
print ('vector number 3 is equal to:\n',vec3, '\n')

#2.3:
print ('2.3: ')
vec4 = vec1 + 2* vec3
print ('vector number 4 is equal to:\n',vec4, '\n')

#2.5:
print ('2.5: ')
vec5 = np.dot(mat1, vec4)
print ('vector number 5 is equal to:\n',vec5, '\n')

#2.6:
print ('2.6: ')
mat1_t = mat1.transpose()
print ('Transpose of mat1 is:\n',mat1_t)

#2.7:
print ('2.7: ')
print ('determinant = ', np.linalg.det(mat1))

#2.8:
print ('2.8: ')
print ('trace = ', np.trace(mat1))

#2.9:
print ('2.9: ')
print ('Smallest element in vec1 = ', np.min(vec1))

#2.10:
print ('2.10: ')
j = np.min(vec1)
print ('Smallest element index in vec1 = ', np.where ( vec1 == j))

#2.11:
print ('2.11: ')
print ('Smallest element in vec1 = ', np.min(mat1))

#2.12:
print ('2.12: ')

#2.13:
print ('2.13: ')
A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])

dict1 = {}
rows = np.sum (A, axis = -1) #sum of rows
dict1['max_row'] = np.max (rows)  #finding max sum of rows
dict1['min_row'] = np.min (rows)  #finding min sum of rows

columns = np.sum(A, axis = -2) #sum of columns
dict1['max_columns'] = np.max (columns)  #finding max sum of columns
dict1['min_columns'] = np.min (columns)  #finding min sum of columns

d1 =  np.diag (A)
dict1['sum_d1'] = np.sum (d1) #finding sum of first diagonal

A2 =  np.fliplr (A)
d2 =  np.diag (A2)
dict1['sum_d2'] = np.sum (d2)  #finding sum of seccond diagonal
values = list (dict1.values())
print (dict1)
v_max = max (values)
v_min = min (values)

if v_max == v_min :
    print ('it is magic square')
else:
    print ('it is not magic square')
#2.14:
print ('2.14: ')
M=np.array([[17, 24, 1, 8, 15, 17, 24, 1, 8, 15], [23, 5, 7, 14, 16, 23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22,4, 6, 13, 20, 22], [10, 12, 19, 21, 3,10, 12, 19, 21, 3], [11, 18, 25, 2, 9,11, 18, 25, 2, 9],[17, 24, 1, 8, 15, 17, 24, 1, 8, 15], [23, 5, 7, 14, 16, 23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22,4, 6, 13, 20, 22], [10, 12, 19, 21, 3,10, 12, 19, 21, 3], [11, 18, 25, 2, 9,11, 18, 25, 2, 9]])
print (M)
MUL = M[:5,:5]
print (MUL)
MUR = M[:5,5:]
print (MUR)
MLL = M[5:,:5]
print (MLL)
MLR = M[5:,:5]
print (MLR)









































