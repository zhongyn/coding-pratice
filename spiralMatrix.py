def spiralMatrix(matrix,n):
	i,j = 0,0
	row_start = 0
	row_end = n-1
	col_start = 0
	col_end = n-1

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
			print matrix[i]
			i = i - 1
		i = i + 1
		j = j + 1

		row_start += 1
		row_end -= 1
		col_start += 1
		col_end -= 1

m = [[1,2],[3,4]]
spiralMatrix(m,2)


