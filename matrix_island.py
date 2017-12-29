import random

def find_islands(mat):
	island_count = 0
	islands = []
	for row_no, row in enumerate(mat):
		for col_no, col in enumerate(row):
			if col == 1:
				island_name = 'i' + str(island_count)
				island_count += 1
				islands.append(island_name)
				mark_and_prop(mat, row_no, col_no, island_name)
	print(f'\nFound {str(island_count)} islands.')
	print('here is the new map:')
	pretty_mat_print(mat)

def mark_and_prop(mat, row, column, island_name):
	mat[row][column] = island_name
	neighbors =  get_neighbors(mat, row, column)
	free_land_neighbors = [(x,y) for x,y in neighbors if mat[x][y] == 1]
	for n in free_land_neighbors:
		mark_and_prop(mat, n[0], n[1], island_name)

def get_neighbors(mat, row, col):
	max_row = len(mat)
	max_col = len(mat[0])
	result = []
	if row > 0:
		result.append((row - 1, col))
	if row < max_row - 1:
		result.append((row + 1, col))
	if col > 0:
		result.append((row, col - 1))
	if col < max_col - 1:
		result.append((row, col + 1))
	return result

def convert_string_map(mat):
	return [[int(n) for n in list(x)] for x in mat]

def make_random_map(row_no, col_no):
	mat = []
	for row in range(row_no):
		row = []
		for col in range(col_no):
			row.append(random.choice([0,1]))
		mat.append(row)
	print('here is the map:')
	pretty_mat_print(mat)
	return mat

def pretty_mat_print(matrix):
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print('\n'.join(table))


sample_mat = [
'001100',
'010100',
'110001',
'000001',
'000100',
'111100']