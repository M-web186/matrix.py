# Program to add two matrices using nested loop

X = [[6,11,4],
    [5,12,3],
    [15,16,2]]

Y = [[8,10,1],
    [9,13,3],
    [4,6,6]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
