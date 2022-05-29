#Do your calculation in the main method in the bottom

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


class MatrixSum:
    pass


class MatrixProduct:
    pass


class BinOperation:
    def __init__(self, x, op, y):
        self.x = x
        self.op = op
        self.y = y


def calculate(binOperation):
    x = binOperation.x
    op = binOperation.op
    y = binOperation.y

    left_matrix = x
    left_cost = 0
    right_matrix = y
    right_cost = 0

    if type(x).__name__ == "BinOperation":  # doing calculations on left expression
        expression = BinOperation(x.x, x.op, x.y)
        left_calculated = calculate(expression)
        left_matrix = left_calculated[0]
        left_cost = left_calculated[1]

    if type(y).__name__ == "BinOperation":  # calculations on right expression
        expression = BinOperation(y.x, y.op, y.y)
        right_calculated = calculate(expression)
        right_matrix = right_calculated[0]
        right_cost = right_calculated[1]

    if op == MatrixSum:  # if matrix sum
        result_matrix = Matrix(left_matrix.rows, left_matrix.columns)
        result_cost = left_matrix.rows * left_matrix.columns + left_cost + right_cost
    elif op == MatrixProduct:  # if matrix product
        result_matrix = Matrix(left_matrix.rows, right_matrix.columns)
        result_cost = (2 * left_matrix.rows * left_matrix.columns * right_matrix.columns) + left_cost + right_cost
    else:
        return "you made a mistake, son", "dumb dumb"

    return result_matrix, result_cost

if __name__ == '__main__':
    # a scalar is Matrix(1, 1)
    # a vector is Matrix(n, 1)
    # a transposed vector is Matrix(1, n)
    # a matrix is Matrix(n, m)

    A = Matrix(10, 70)
    B = Matrix(70, 30)
    C = Matrix(10, 30)

    # the expression (AB)C is done below
    expression = BinOperation(BinOperation(A, MatrixProduct, B), MatrixSum, C)
    result = calculate(expression)

    print(f'Cost is: {result[1]}')