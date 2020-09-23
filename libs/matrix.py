
from errors import MatrixSizeMismatchError, MatrixIndexOutOfBoundsError, MatrixHasNoInverseError


class Matrix (object):

  def __init__(self, nrows, ncols, data=None, init_val=0):
    """
    A 2D matrix class.
    :param nrows: The height of the matrix (number of rows)
    :param ncols: The width of the matrix (number of columns)
    :param data: A list of values to populate the matrix. Must be the exact size of the matrix (width * height) in length.
    :param init_val: If data is not provided, an initializing value can be used instead. Each number in the matrix will be this value.
    """
    self._nrows = nrows
    self._ncols = ncols
    # The matrix numbers are stored in a 2D list.
    self._data = [init_val for _ in range(self._ncols * self._nrows)]
    if data is not None:
      self.set_all(data)

  def inverse(self):
    """
    Get the inverse of the matrix if it exists, otherwise raise a MatrixHasNoInverseError

    :raises MatrixHasNoInverseError: if no inverse exists for this matrix
    :return: a new matrix inverse to this one.
    """
    new_mtx = Matrix(self._nrows, self._ncols)
    # step 1. Create a matrix of minors, taking the determinants of the submatrices
    for row in range(self._nrows):
      for col in range(self._ncols):
        val = self.get_sub_matrix(row, col).get_determinant()
        # step 2. Apply the checkerboard of alternating signs to the matrix values
        val * ((-1) ** (row + col))
        new_mtx.set(row, col, val)
    # step 3. Transpose the matrix
    new_mtx = new_mtx.transpose()
    # step 4. Multiply the matrix by (1/d), where 'd' is the original matrix's determinant
    d = self.get_determinant()
    if d == 0:
      raise MatrixHasNoInverseError()
    return new_mtx * (1 / d)

  def add(self, mtx):
    """
    :param mtx: the matrix to add to this one
    :raises MatrixSizeMismatchError: if the provided matrix doesn't match the size of this one
    :return: a new matrix with the result of the addition.
    """
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to add. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    return Matrix(self._nrows, self._ncols, list(map(lambda a: a[0] + a[1], list(zip(self._data, mtx._data)))))

  def subtract(self, mtx):
    """
    :param mtx: the matrix to subtract from this one
    :raises MatrixSizeMismatchError: if the provided matrix doesn't match the size of this one
    :return: a new matrix with the result of the subtraction.
    """
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to subtract. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    return Matrix(self._nrows, self._ncols, list(map(lambda a: a[0] - a[1], list(zip(self._data, mtx._data)))))
    
  def add_const(self, const):
    """
    :param const: a value to add to each number in the matrix
    :return: a new matrix with the constant added to each numberj
    """
    return Matrix(self._nrows, self._ncols, [d + const for d in self._data])

  def divide(self, const):
    """
    :param const: a value to divide each number by in the matrix
    :raises ZeroDivisionError: if the number provided is 0
    :return: a new matrix with each number divided by the constant
    """
    if const == 0:
      raise ZeroDivisionError("The constant provided cannot be 0.")
    return Matrix(self._nrows, self._ncols, [d / const for d in self._data])

  def int_divide(self, const):
    """
    :param const: a value to integer divide each number by in the matrix
    :raises ZeroDivisionError: if the number provided is 0
    :return: a new matrix with each number integer divided by the constant
    """
    if const == 0:
      raise ZeroDivisionError("The integer provided cannot be 0.")
    return Matrix(self._nrows, self._ncols, [d // const for d in self._data])

  def scale(self, scalar):
    """
    :param scalar: The value by which each number in the matrix will be multiplied
    :return: a new matrix with each number multiplied by the provided scalar
    """
    return Matrix(self._nrows, self._ncols, [d * scalar for d in self._data])

  def negative(self):
    """
    :return: a new matrix with each number's sign flipped
    """
    return self.scale(-1)

  def dot(self, mtx):
    """
    :param mtx: The matrix to dot with this one.
    :raises MatrixSizeMismatchError: if the provided matrix's number of rows doesn't match this matrix's number of columns
    :return: a new matrix that results from dotting this matrix with the one provided.
    """
    if self._ncols != mtx._nrows:
      raise MatrixSizeMismatchError("The height of the provided matrix [%s] must match the width of the original matrix [%s] when performing the dot operation." % (mtx._nrows, self._ncols))
    new_mtx = Matrix(self._nrows, mtx._ncols)
    for row in range(self._nrows):
      for col in range(mtx._ncols):
        r = self.get_row(row)
        c = mtx.get_col(col)
        new_mtx.set(row, col, sum(list(map(lambda a: a[0]*a[1], list(zip(r, c))))))
    return new_mtx

  def transpose(self):
    """
    :return: a new matrix that's been flipped along it's diagonal axis
    """
    new_mtx = Matrix(self._ncols, self._nrows)
    for row in range(self._nrows):
      for col in range(self._ncols):
        new_mtx.set(col, row, self.get(row, col))
    return new_mtx

  def get_row(self, idx):
    """
    :param idx: the index of the row to retrieve from the matrix
    :raises MatrixIndexOutOfBoundsError: if the given index is out of bounds.
    :return: A list of numbers representing the row at the given index (base 0)
    """
    if idx not in range(0, self._nrows):
      raise MatrixIndexOutOfBoundsError("Given row index [%s] is out of bounds for the number of rows [%s]." % (idx, self._nrows))
    return self._data[idx * self._ncols: idx * self._ncols + self._ncols]

  def get_col(self, idx):
    """
    :param idx: the index of the column to retrieve from the matrix
    :raises MatrixIndexOutOfBoundsError: if the given index is out of bounds.
    :return: A list of numbers representing the column at the given index (base 0)
    """
    if idx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given column index [%s] is out of bounds for the number of columns [%s]." % (idx, self._ncols))
    return self._data[idx::self._ncols]

  def get(self, rowidx, colidx):
    """
    :param rowidx: the index of the row
    :param colidx: the index of the column
    :raises MatrixIndexOutOfBoundsError: if the given coordinates are out of the bounds of the matrix
    :return: The number value at the given row and column indices in the matrix
    """
    if rowidx not in range(0, self._nrows) or colidx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    return self._data[rowidx * self._ncols + colidx]

  def set(self, rowidx, colidx, value):
    """
    Set the value at the given row and column index to the value provided
    :param rowidx: the index of the row to edit
    :param colidx: the index of the column to edit
    :raises MatrixIndexOutOfBoundsError: if the given coordinates are out of the bounds of the matrix
    :param value: the value to put in the matrix
    """
    if rowidx not in range(0, self._nrows) or colidx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    self._data[rowidx * self._ncols + colidx] = value
    
  def set_all(self, data):
    """
    Set all the number values for this matrix.
    :raises MatrixIndexOutOfBoundsError: if the length of the list of data doesn't match the size of the matrixj
    :param data: a list of values equal in length to this matrix's (height * width)
    """
    if len(data) != self._nrows * self._ncols:
      raise MatrixSizeMismatchError('The size of the data [%s] does not match the dimensions of the matrix [%s = %s]' % (len(data), self.dimensions, self._nrows * self._ncols))
    self._data = data

  def get_sub_matrix(self, rowidx, colidx):
    """
    Returns the resulting matrix when the row and column at the given indices are removed. Useful for determining
    the inverse and determinant.j
    :param rowidx: the index of the row to remove
    :param colidx: the index of the column to remove
    :raises MatrixIndexOutOfBoundsError: if the given indices fall outside the matrix's bounds
    :return: a new matrix missing the row and column at the specified indices from the original matrix
    """
    if rowidx not in range(0, self._nrows) or colidx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate[(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    new_mtx = Matrix(self._nrows - 1, self._ncols - 1)
    data = []
    for row in range(self._nrows):
      if row == rowidx:
        continue
      for col in range(self._ncols):
        if col == colidx:
          continue
        data.append(self.get(row, col))
    new_mtx._data = data
    return new_mtx

  def get_determinant(self):
    """
    :raises MatrixSizeMismatchError: if attempting to perform this operation on a non-square matrix
    :return: The value of the determinant of this matrix
    """
    if self._nrows != self._ncols:
      raise MatrixSizeMismatchError(
        "The determinant operation can only be performed on square matrices. Matrix dimensions: [%s]." % self.dimensions)
    # if only a 1x1 matrix, return the single value
    if self._nrows == 1:
      return self._data[0]
    # if a 2x2, return the a*d - b*c of its values
    elif self._nrows == 2:
      a, b, c, d = self._data
      return a * d - b * c
    # if larger than 2x2, recursively perform the determinants on the submatrices
    else:
      mult = 1
      total = 0
      for col, d in enumerate(self.get_row(0)):
        total += mult * d * self.get_sub_matrix(0, col).get_determinant()
        mult *= -1
      return total

  @property
  def num_rows(self):
    return self._nrows

  @property
  def num_cols(self):
    return self._ncols

  @property
  def dimensions(self):
    """
    :return: A tuple containing the number of (rows, columns) in this matrix
    """
    return self._nrows, self._ncols

  def __add__(self, mtx):
    if type(mtx) is Matrix:
      return self.add(mtx)
    elif type(mtx) in [int, float]:
      return self.add_const(mtx)
    else:
      raise TypeError("Cannot add type [%s] to a matrix." % type(mtx))
    
  def __sub__(self, mtx):
    if type(mtx) is Matrix:
      return self.subtract(mtx)
    elif type(mtx) in [int, float]:
      return self.add_const(-1 * mtx)
    else:
      raise TypeError("Cannot subtract type [%s] from a matrix." % type(mtx))

  def __mul__(self, mtx):
    if type(mtx) is Matrix:
      return self.dot(mtx)
    elif type(mtx) in [int, float]:
      return self.scale(mtx)
    else:
      raise TypeError("Cannot multiply type [%s] with a matrix." % type(mtx))

  def __floordiv__(self, const):
    if type(const) in [int, float]:
      return self.int_divide(const)
    else:
      raise TypeError("Cannot int divide a matrix by type [%s]." % type(const))

  def __truediv__(self, const):
    if type(const) in [int, float]:
      return self.divide(const)
    else:
      raise TypeError("Cannot divide a matrix by type [%s]." % type(const))

  def __neg__(self):
    return self.negative()
    
  def __repr__(self):
    s = '['
    for i in range(self._nrows):
      s += '[%s]' % ', '.join([str(n) for n in self.get_row(i)])
      if i < self._nrows - 1:
        s += ',\n '
    return s + ']'


class IdentityMatrix(Matrix):
  def __init__(self, size):
    super().__init__(size, size, [1] + ([0] * size + [1]) * (size - 1))
