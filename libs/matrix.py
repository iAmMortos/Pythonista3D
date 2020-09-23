
from errors import MatrixSizeMismatchError, MatrixIndexOutOfBoundsError


class Matrix (object):

  def __init__(self, nrows, ncols, init_val=0):
    self._nrows = nrows
    self._ncols = ncols
    self._data = [[init_val for _ in range(self._ncols)] for _ in range(self._nrows)]

  def inverse(self):
    pass

  def add(self, mtx):
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to add. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    new_mtx = Matrix(self._nrows, self._ncols)
    for rowidx in range(self._nrows):
      for colidx in range(self._ncols):
        new_mtx.set(rowidx, colidx, self.get(rowidx, colidx) + mtx.get(rowidx, colidx))
    return new_mtx

  def subtract(self, mtx):
    if self.dimensions != mtx.dimensions:
      raise MatrixSizeMismatchError("Matrices must be the same dimensions to subtract. [%s] and [%s] provided." % self.dimensions, mtx.dimensions)
    new_mtx = Matrix(self._nrows, self._ncols)
    for rowidx in range(self._nrows):
      for colidx in range(self._ncols):
        new_mtx.set(rowidx, colidx, self.get(rowidx, colidx) - mtx.get(rowidx, colidx))
    return new_mtx

  def scale(self, scalar):
    new_mtx = Matrix(self._nrows, self._ncols)
    for rowidx in range(self._nrows):
      for colidx in range(self._ncols):
        self._data[rowidx][colidx] *= scalar
    return new_mtx

  def negative(self):
    return self.scale(-1)

  def dot(self, mtx):
    pass

  def cross(self, mtx):
    pass

  def transpose(self):
    pass

  def get_row(self, idx):
    if idx not in range(0, self._nrows + 1):
      raise MatrixIndexOutOfBoundsError("Given row index [%s] is out of bounds for the number of rows [%s]." % (idx, self._nrows))
    return self._data[idx]

  def get_col(self, idx):
    if idx not in range(0, self._ncols + 1):
      raise MatrixIndexOutOfBoundsError("Given column index [%s] is out of bounds for the number of columns [%s]." % (idx, self._ncols))
    return [self._data[row][idx] for row in self._data]

  def get(self, rowidx, colidx):
    if rowidx not in range(0, self._nrows + 1) or colidx not in range(0, self._ncols + 1):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    return self._data[rowidx][colidx]

  def set(self, rowidx, colidx, value):
    if rowidx not in range(0, self._nrows + 1) or colidx not in range(0, self._ncols + 1):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    self._data[rowidx][colidx] = value

  def __repr__(self):
    s = '['
    for row in range(self._nrows):
      s += '[%s]' % (', '.join(self.get_row(row)))
      if row != self._nrows - 1:
        s += ",\n "
    s += ']'
    return s

  @property
  def num_rows(self):
    return self._nrows

  @property
  def num_cols(self):
    return self._ncols

  @property
  def dimensions(self):
    return self._nrows, self._ncols


if __name__ == '__main__':
  pass
  # Test code