
from errors import MatrixSizeMismatchError, MatrixIndexOutOfBoundsError, MatrixHasNoInverseError


class Matrix (object):

  def __init__(self, nrows, ncols, data=None, init_val=0):
    self._nrows = nrows
    self._ncols = ncols
    self._data = [init_val for _ in range(self._ncols * self._nrows)]
    if data is not None:
      self.set_all(data)

  def inverse(self):
    new_mtx = Matrix(self._nrows, self._ncols)
    for row in range(self._nrows):
      for col in range(self._ncols):
        new_mtx.set(row, col, self.get_sub_matrix(row, col).determinant * ((-1) ** (row + col)))
    new_mtx = new_mtx.transpose()
    d = self.determinant
    if d == 0:
      raise MatrixHasNoInverseError()
    return new_mtx * (1 / d)

  def add(self, mtx):
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to add. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    return Matrix(self._nrows, self._ncols, list(map(lambda a: a[0] + a[1], list(zip(self._data, mtx._data)))))

  def subtract(self, mtx):
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to subtract. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    return Matrix(self._nrows, self._ncols, list(map(lambda a: a[0] - a[1], list(zip(self._data, mtx._data)))))
    
  def add_const(self, const):
    return Matrix(self._nrows, self._ncols, [d + const for d in self._data])

  def divide(self, const):
    if const == 0:
      raise ZeroDivisionError("The constant provided cannot be 0.")
    return Matrix(self._nrows, self._ncols, [d / const for d in self._data])

  def int_divide(self, const):
    if const == 0:
      raise ZeroDivisionError("The integer provided cannot be 0.")
    return Matrix(self._nrows, self._ncols, [d // const for d in self._data])

  def scale(self, scalar):
    return Matrix(self._nrows, self._ncols, [d * scalar for d in self._data])

  def negative(self):
    return self.scale(-1)

  def dot(self, mtx):
    if self._ncols != mtx._nrows:
      raise MatrixSizeMismatchError("The height of the provided matrix [%s] must match the width of the original matrix [%s] when performing the dot operation." % (mtx._nrows, self._ncols))
    new_mtx = Matrix(self._nrows, mtx._ncols)
    for row in range(self._nrows):
      for col in range(mtx._ncols):
        r = self.get_row(row)
        c = mtx.get_col(col)
        new_mtx.set(row, col, sum(list(map(lambda a: a[0]*a[1], list(zip(r, c))))))
    return new_mtx

  def cross_product(self):
    pass

  def transpose(self):
    new_mtx = Matrix(self._ncols, self._nrows)
    for row in range(self._nrows):
      for col in range(self._ncols):
        new_mtx.set(col, row, self.get(row, col))
    return new_mtx

  def get_row(self, idx):
    if idx not in range(0, self._nrows):
      raise MatrixIndexOutOfBoundsError("Given row index [%s] is out of bounds for the number of rows [%s]." % (idx, self._nrows))
    return self._data[idx * self._ncols: idx * self._ncols + self._ncols]

  def get_col(self, idx):
    if idx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given column index [%s] is out of bounds for the number of columns [%s]." % (idx, self._ncols))
    return self._data[idx::self._ncols]

  def get(self, rowidx, colidx):
    if rowidx not in range(0, self._nrows) or colidx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    return self._data[rowidx * self._ncols + colidx]

  def set(self, rowidx, colidx, value):
    if rowidx not in range(0, self._nrows) or colidx not in range(0, self._ncols):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    self._data[rowidx * self._ncols + colidx] = value
    
  def set_all(self, data):
    if len(data) != self._nrows * self._ncols:
      raise MatrixSizeMismatchError('The size of the data [%s] does not match the dimensions of the matrix [%s = %s]' % (len(data), self.dimensions, self._nrows * self._ncols))
    self._data = data

  def get_sub_matrix(self, rowidx, colidx):
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

  @property
  def num_rows(self):
    return self._nrows

  @property
  def num_cols(self):
    return self._ncols

  @property
  def dimensions(self):
    return self._nrows, self._ncols

  @property
  def determinant(self):
    if self._nrows != self._ncols:
      raise MatrixSizeMismatchError("The determinant operation can only be performed on square matrices. Matrix dimensions: [%s]." % self.dimensions)
    if self._nrows == 1:
      return self._data[0]
    elif self._nrows == 2:
      a, b, c, d = self._data
      return a * d - b * c
    else:
      mult = 1
      total = 0
      for col,d in enumerate(self.get_row(0)):
        total += mult * d * self.get_sub_matrix(0, col).determinant
        mult *= -1
      return total
    
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
