
from errors import MatrixSizeMismatchError, MatrixIndexOutOfBoundsError


class Matrix (object):

  def __init__(self, nrows, ncols, data=None, init_val=0):
    self._nrows = nrows
    self._ncols = ncols
    self._data = [init_val for _ in range(self._ncols * self._nrows)]
    if data is not None:
      self.set_all(data)

  def inverse(self):
    pass

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

  def scale(self, scalar):
    return Matrix(self._nrows, self._ncols, [d * scalar for d in self._data])

  def negative(self):
    return self.scale(-1)

  def dot(self, mtx):
    pass

  def cross(self, mtx):
    pass

  def transpose(self):
    pass

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
    if rowidx not in range(0, self._nrows + 1) or colidx not in range(0, self._ncols + 1):
      raise MatrixIndexOutOfBoundsError("Given matrix coordinate [(%s, %s)] is out of bounds of the matrix of dimension [%s]." % (rowidx, colidx, self.dimensions))
    self._data[rowidx * self._ncols + colidx] = value
    
  def set_all(self, data):
    if len(data) != self._nrows * self._ncols:
      raise MatrixSizeMismatchError('The size of the data [%s] does not match the dimensions of the matrix [%s = %s]' % (len(data), self.dimensions, self._nrows * self._ncols))
    self._data = data

  @property
  def num_rows(self):
    return self._nrows

  @property
  def num_cols(self):
    return self._ncols

  @property
  def dimensions(self):
    return self._nrows, self._ncols
    
  def __add__(self, mtx):
    if type(mtx) is Matrix:
      return self.add(mtx)
    elif type(mtx) is int or type(mtx) is float:
      return self.add_const(mtx)
    
  def __sub__(self, mtx):
    return self.subtract(mtx)
    
  def __repr__(self):
    s = '['
    for i in range(self._nrows):
      s += '[%s]' % ', '.join([str(n) for n in self.get_row(i)])
      if i < self._nrows - 1:
        s += ',\n '
    return s + ']'

