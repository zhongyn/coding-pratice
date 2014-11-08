def spiralMatrix(matrix,rows,columns):
	i,j = 0,0
	row_start = 0
	row_end = rows-1
	col_start = 0
	col_end = columns-1

	while (row_start<=row_end or col_start<=col_end):

		while j <= col_end:
			print matrix[i][j]
			j = j + 1
		j = j - 1
		i = i + 1

		while i <= row_end:
			print matrix[i][j]
			i = i + 1
		i = i - 1
		j = j - 1

		while j >= col_start:
			print matrix[i][j]
			j = j - 1
		j = j + 1
		i = i - 1

		while i > row_start:
			print matrix[i][j]
			i = i - 1
		i = i + 1
		j = j + 1

		row_start += 1
		row_end -= 1
		col_start += 1
		col_end -= 1

m = [[1,2,3],[4,5,6],[7,8,9]]
# spiralMatrix(m,3)


def counterSpiralMatrix(matrix,rows,columns):
	row_start = 0
	row_end = rows-1
	col_start = 0
	col_end = columns-1

	while (row_start<=row_end or col_start<=col_end):

		for k in range(col_start,col_end+1):
			print matrix[row_start][k]

		for k in range(row_start+1,row_end+1):
			print matrix[k][col_end]

		for k in range(col_end-1,col_start-1,-1):
			print matrix[row_end][k]

		for k in range(row_end-1,row_start,-1):
			print matrix[k][col_start]

		row_start += 1
		row_end -= 1
		col_start += 1
		col_end -= 1

matrix = []
for i in range(4):
	matrix.append([j+i*4 for j in range(1,5)])

counterSpiralMatrix(matrix,4,4)





