import math
from pythonista3d.errors import VectorSizeMismatchError
from pythonista3d.points import Point
from numbers import Number
from typing import Union


class Vector(Point):
  def __init__(self, *vals: Number):
    """
    Represents an n-dimensional vector
    :param vals: the values in the vector
    """
    super().__init__(*vals)

  def add(self, vec: "Vector") -> "Vector":
    """
    :param vec: The vector to add to this one
    :return: A new vector containing the result of the addition
    """
    if self.num_dimensions != vec.num_dimensions:
      raise VectorSizeMismatchError("Vertices must be the same dimensions to add. [%s] and [%s] provided." %
                                    (self.num_dimensions, vec.num_dimensions))
    return self.__class__(*[self[i] + vec[i] for i in range(self.num_dimensions)])

  def subtract(self, vec: "Vector") -> "Vector":
    """
    :param vec: The vector to subtract from this one
    :return: A new vector containing the result of the subtraction
    """
    if self.num_dimensions != vec.num_dimensions:
      raise VectorSizeMismatchError("Vertices must be the same dimensions to subtract. [%s] and [%s] provided." %
                                    (self.num_dimensions, vec.num_dimensions))
    return self.__class__(*[self[i] - vec[i] for i in range(self.num_dimensions)])

  def add_const(self, const: Number):
    """
    :param const: the constant value to add to each element of the vector
    :return: A new vector with each value increased by the given const.
    """
    return self.__class__(*[self[i] + const for i in range(self.num_dimensions)])

  def add_to_point(self, pt: "Point") -> "Point":
    """
    :param pt:
    :return:
    """
    if self.num_dimensions != pt.num_dimensions:
      raise VectorSizeMismatchError("The dimension size of the point and the vector being added must match. Point size: [%s], Vector size: [%s]" % pt.num_dimensions, self.num_dimensions)
    return pt.__class__(*[pt._vals[i] + self._vals[i] for i in range(self.num_dimensions)])

  def subtract_const(self, const: Number):
    """
    :param const: the constant value to subtract from each element of the vector
    :return: A new vector with each value subtracted by the given const.
    """
    return self.__class__(*[self[i] - const for i in range(self.num_dimensions)])

  def subtract_from_point(self, pt: "Point") -> "Point":
    """
    :param pt:
    :return:
    """
    if self.num_dimensions != pt.num_dimensions:
      raise VectorSizeMismatchError("The dimension size of the point and the vector being added must match. Point size: [%s], Vector size: [%s]" % pt.num_dimensions, self.num_dimensions)
    return pt.__class__(*[pt._vals[i] - self._vals[i] for i in range(self.num_dimensions)])

  def scale(self, scalar: Number) -> "Vector":
    """
    Scale the entire vector by the given scalar value.
    :param scalar: The value by which to scale the vector.
    :return: A new vector containing the scaled result.
    """
    return self.__class__(*[self[i] * scalar for i in range(self.num_dimensions)])

  def normalize(self) -> "Vector":
    """
    Produce a unit version of this vector.
    :return: A new vector containing the unit version of this vector.
    """
    m = self.get_magnitude()
    return self.__class__(*[n / m for n in self._vals])

  def get_magnitude(self):
    """
    :return: The computed magnitude of this vector.
    """
    return math.sqrt(sum([n ** 2 for n in self._vals]))

  def dot(self, vec: "Vector") -> Number:
    """
    Dot the given vector with this vector.
    :param vec: The vector with which to dot this vector
    :return: the result of the dot operation
    :raises: VectorSizeMismatchError if the number of dimensions of the two vectors don't match
    """
    if self._num_dimensions != vec._num_dimensions:
      raise VectorSizeMismatchError("A vector may only be dotted with a vector of identical dimensions. " +
                                    "Vectors of length [%s] and [%s] provided." %
                                    (self._num_dimensions, vec._num_dimensions))
    return sum([z[0] * z[1] for z in zip(self._vals, vec._vals)])
    
  def as_point(self):
    return Point(*self._vals)
    
  @staticmethod
  def from_point(pt):
    return Vector(*pt.as_list())

  def __add__(self, other: Union["Vector", "Point", Number]) -> Union["Vector", "Point"]:
    if isinstance(other, Vector):
      return self.add(other)
    elif isinstance(other, Number):
      return self.add_const(other)
    elif isinstance(other, Point):
      return self.add_to_point(other)
    else:
      raise TypeError("Cannot add type [%s] to a vector." % type(other))

  def __radd__(self, other: Number) -> "Vector":
    return self.__add__(other)

  def __sub__(self, other: Union["Vector", "Point", Number]) -> Union["Vector", "Point"]:
    if isinstance(other, Vector):
      return self.subtract(other)
    elif isinstance(other, Number):
      return self.subtract_const(other)
    elif isinstance(other, Point):
      return self.subtract_from_point(other)
    else:
      raise TypeError("Cannot subtract type [%s] from a vector." % type(other))

  def __mul__(self, other: Union["Vector", Number]) -> Union["Vector", Number]:
    if isinstance(other, Vector):
      return self.dot(other)
    elif isinstance(other, Number):
      return self.scale(other)
    else:
      raise TypeError("Cannot multiply type [%s] with a vector." % type(other))

  def __rmul__(self, other: Number) -> "Vector":
    return self.__mul__(other)

  def __neg__(self) -> "Vector":
    return self.__class__(*[-v for v in self._vals])

  def __truediv__(self, other):
    return self.scale(1 / other)

class Vector2D(Vector):
  def __init__(self, x: Number = 0, y: Number = 0):
    """
    A two-dimensional vector
    :param x:
    :param y:
    """
    super().__init__(x, y)

  def cross(self) -> "Vector2D":
    """
    :return: A new vector: the cross of this 2D vector.
    """
    return Vector2D(-self.y, self.x)

  @property
  def x(self):
    return self[0]

  @x.setter
  def x(self, val: Number):
    self[0] = val

  @property
  def y(self):
    return self[1]

  @y.setter
  def y(self, val: Number):
    self[1] = val


class Vector3D(Vector):
  def __init__(self, x: Number = 0, y: Number = 0, z: Number = 0):
    """
    A three-dimensional vector
    :param x:
    :param y:
    :param z:
    """
    super().__init__(x, y, z)

  def cross(self, vec: "Vector3D") -> "Vector3D":
    """
    :param vec: The vector with which to cross this 3D vector
    :return: A new vector with the result of this vector crossed with the given vector.
    """
    return Vector3D(self.y * vec.z - self.z * vec.y,
                    self.z * vec.x - self.x * vec.z,
                    self.x * vec.y - self.y * vec.x)

  @property
  def x(self):
    return self[0]

  @x.setter
  def x(self, val: Number):
    self[0] = val

  @property
  def y(self):
    return self[1]

  @y.setter
  def y(self, val: Number):
    self[1] = val

  @property
  def z(self):
    return self[2]

  @z.setter
  def z(self, val: Number):
    self[2] = val
