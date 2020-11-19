def build_matrix(n):
    matrix = [];
    if n > 0:
        for i in range(n):
            matrix.extend([[-1]*n])
    return matrix

