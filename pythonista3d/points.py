
from numbers import Number


class Point(object):
  def __init__(self, ndims, *vals):
    """
    Represents a point in n-dimension
    :param ndims: the number of dimensions
    :param vals: the n values for this point (must match ndims)
    """
    self._num_dimensions = ndims
    self._vals = vals[::]
    if len(vals) != ndims:
      raise ValueError("The number of values provided must match the `ndims` provided.")

  def __len__(self):
    return self._num_dimensions

  def __getitem__(self, item):
    if not isinstance(item, int):
      raise TypeError("The key provided [%s] must be an integer index." % item)
    if item not in range(0, self._num_dimensions):
      raise ValueError("They key provided [%s] is outside the bounds of the number of dimensions [%s]." % (item, self._num_dimensions))
    return self._vals[item]

  def __setitem__(self, key, value):
    if not isinstance(key, int):
      raise TypeError("The key provided [%s] must be an integer index." % key)
    if key not in range(0, self._num_dimensions):
      raise ValueError("They key provided [%s] is outside the bounds of the number of dimensions [%s]." % (key, self._num_dimensions))
    if not isinstance(value, Number):
      raise TypeError("The value provided must be a numerical value")
    self._vals[key] = value

  @property
  def num_dimensions(self):
    """
    Getter.
    :return: the number of dimensions at this point.
    """
    return self._num_dimensions


class Point2D(Point):
  def __init__(self, x=0, y=0):
    """
    Represents a 2-dimensional coordinate point. Default values for x and y are 0 if not explicitly set.
    :param x:
    :param y:
    """
    super().__init__(2, x, y)

  @property
  def x(self):
    return self[0]

  @x.setter
  def x(self, val):
    self[0] = val

  @property
  def y(self):
    return self[1]

  @y.setter
  def y(self, val):
    self[1] = val


class Point3D(Point):
  def __init__(self, x=0, y=0, z=0):
    """
    Represents a 3-dimensional coordinate point. Default values for x, y, and z are 0 if not explicitly set.
    :param x:
    :param y:
    :param z:
    """
    super().__init__(3, x, y, z)

  @property
  def x(self):
    return self[0]

  @x.setter
  def x(self, val):
    self[0] = val

  @property
  def y(self):
    return self[1]

  @y.setter
  def y(self, val):
    self[1] = val

  @property
  def z(self):
    return self[2]

  @z.setter
  def z(self, val):
    self[2] = val
