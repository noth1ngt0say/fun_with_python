def load_matrix(filename):
    f = open('matrix.txt', 'r', encoding='utf-8')
    mat = [list(map(int, line.split())) for line in f]
    f.close()
    if all(map(lambda row: len(row) == len(mat[0]), mat)):
        return mat
    else:
        return False
print(load_matrix('matrix.txt'))