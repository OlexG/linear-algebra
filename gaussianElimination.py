import numpy as np

inp = input("Enter an equation matrix, \
rows separated by ',' and collumns by ' ' ")

mat = np.array([i.split() for i in inp.split(',')])
mat = mat.astype(float)

# start with making the 1st element of 1st row 1

if (mat.shape[0] != mat.shape[1] - 1):
	print("invalid input")
	exit()


for x in range(0, mat.shape[0] - 1):
	mat[x] = mat[x] / mat[x][x]
	for y in range(x + 1, mat.shape[0]):
		mat[y] -= (mat[x] * mat[y][x])

for x in reversed(range(1, mat.shape[0])):
	mat[x] = mat[x] / mat[x][x]
	for y in range(0, x):
		mat[y] = mat[y] - (mat[x] * mat[y][x])
mat[0] = mat[0] / mat[0][0]

print("Resulting matrix with variable values in the last collumn")
print(mat)