
from typing import List
from numbers import Number

# TODO: document fully


class Point(object):
  def __init__(self, *vals: Number):
    """
    Represents a point in n-dimension
    :param vals: the n values for this point (must match ndims)
    """
    self._vals = list(vals[::])
    self._num_dimensions = len(vals)

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

  def as_list(self) -> List[Number]:
    """
    :return: a copy of the values in the point as a list
    """
    return self._vals[::]

  def __repr__(self):
    return '({})'.format(', '.join([str(n) for n in self._vals]))

  @property
  def num_dimensions(self) -> int:
    """
    Getter.
    :return: the number of dimensions at this point.
    """
    return self._num_dimensions


class Point2D(Point):
  def __init__(self, x: Number = 0, y: Number = 0):
    """
    Represents a 2-dimensional coordinate point. Default values for x and y are 0 if not explicitly set.
    :param x:
    :param y:
    """
    super().__init__(x, y)

  @property
  def x(self) -> Number:
    return self[0]

  @x.setter
  def x(self, val: Number):
    self[0] = val

  @property
  def y(self) -> Number:
    return self[1]

  @y.setter
  def y(self, val: Number):
    self[1] = val

  def __repr__(self):
    return '(x: {}, y: {})'.format(self.x, self.y)


class Point3D(Point):
  def __init__(self, x: Number = 0, y: Number = 0, z: Number = 0):
    """
    Represents a 3-dimensional coordinate point. Default values for x, y, and z are 0 if not explicitly set.
    :param x:
    :param y:
    :param z:
    """
    super().__init__(x, y, z)

  @property
  def x(self) -> Number:
    return self[0]

  @x.setter
  def x(self, val: Number):
    self[0] = val

  @property
  def y(self) -> Number:
    return self[1]

  @y.setter
  def y(self, val: Number):
    self[1] = val

  @property
  def z(self) -> Number:
    return self[2]

  @z.setter
  def z(self, val: Number):
    self[2] = val

  def __repr__(self):
    return '(x: {}, y: {}, z: {})'.format(self.x, self.y, self.z)
