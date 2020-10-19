
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point2D
from numbers import Number
from enum import Enum


class ReflectionLine2D(Enum):
  """
  Represents the different lines of reflection in 2D space
  """
  x = "x"
  y = "y"
  origin = "origin"
  xy = "xy"


class Transform2D(object):
  """
  Contains the means of translating things in 2 dimensions using matrix math.
  Can perform transformations on individual points, or can provide the appropriate matrix by which
  the transformation can be performed
  """

  @staticmethod
  def rotation_matrix(rads: Number) -> "Matrix":
    """
    :param rads: the amount of desired rotation (in radians)
    :return: A matrix representing the desired rotation operationj
    """
    return Matrix(3, 3, [math.cos(rads), -math.sin(rads), 0,
                         math.sin(rads), math.cos(rads), 0,
                         0, 0, 1])

  @staticmethod
  def rotate(pt: "Point2D", rads: Number) -> "Point2D":
    """
    Rotate a given point by the amount specified (in radians)
    :param pt: a 2D Point to rotate
    :param rads: the amount of desired rotation (in radians)j
    :return: A point that has been rotated by the given amount
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.rotation_matrix(rads)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def scaling_matrix(xscale: Number, yscale: Number) -> "Matrix":
    """
    :param xscale: the amount of scaling in the x direction
    :param yscale: the amount of scaling in the y direction
    :return: A matrix representing the desired scale operation
    """
    return Matrix(3, 3, [xscale, 0, 0,
                         0, yscale, 0,
                         0, 0, 1])

  @staticmethod
  def scale(pt: "Point2D", xscale: Number, yscale: Number) -> "Point2D":
    """
    Scale a given point by the xscale and yscale amounts
    :param pt: a 2D Point to scale
    :param xscale: the amount of scaling in the x direction
    :param yscale: the amount of scaling in the y direction
    :return: A scaled point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.scaling_matrix(xscale, yscale)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def shearing_matrix(horizontal: Number, vertical: Number) -> "Matrix":
    """
    :param horizontal: The amount of horizontal shear
    :param vertical: The amount of vertical shear
    :return: A matrix representing the desired shearing operation
    """
    return Matrix(3, 3, [1, horizontal, 0,
                         vertical, 1, 0,
                         0, 0, 1])

  @staticmethod
  def shear(pt: "Point2D", horizontal: Number, vertical: Number) -> "Point2D":
    """
    Shear a given point by the horizontal and vertical amount specified
    :param pt: a 2D Point to shear
    :param horizontal: The amount of horizontal shear
    :param vertical: The amount of vertical shear
    :return: A sheared point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.shearing_matrix(horizontal, vertical)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def translation_matrix(dx: Number, dy: Number) -> "Matrix":
    """
    :param dx: change in the x direction
    :param dy: change in the y direction
    :return: A matrix representing the desired translation operation
    """
    return Matrix(3, 3, [1, 0, dx,
                         0, 1, dy,
                         0, 0, 1])

  @staticmethod
  def translate(pt: "Point2D", dx: Number, dy: Number) -> "Point2D":
    """
    Translate the given point by the x and y amounts specified
    :param pt: a 2D point to translate
    :param dx: change in the x direction
    :param dy: change in the y direction
    :return: A translated point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.translation_matrix(dx, dy)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def reflection_matrix(line: "ReflectionLine2D") -> Matrix:
    """
    :param line: the line over which the reflection should be performed
    :return: A matrix representing the desired reflection operation
    """
    d = {ReflectionLine2D.x: [1, 0, 0,
                              0, -1, 0,
                              0, 0, 1],
         ReflectionLine2D.y: [-1, 0, 0,
                              0, 1, 0,
                              0, 0, 1],
         ReflectionLine2D.origin: [-1, 0, 0,
                                   0, -1, 0,
                                   0, 0, 1],
         ReflectionLine2D.xy: [0, 1, 0,
                               1, 0, 0,
                               0, 0, 1]}
    return Matrix(3, 3, d[line])

  @staticmethod
  def reflect(pt: "Point2D", line: "ReflectionLine2D") -> "Point2D":
    """
    Reflect the given point over the specified reflection line
    :param pt: a 2D point to reflect
    :param line: a ReflectionLine2D value specifying the line of reflection
    :return: A reflected point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.reflection_matrix(line)
    return Point2D(*(tmx * pmx).as_list()[:2])


class Transform2DBuilder(object):
  def __init__(self):
    """
    Composites multiple transformations into a single transformation matrix for efficiency of computation.
    Can produce the actual finished matrix, or apply the matrix to a given 2D point.
    """
    self._mtx = Matrix.identity_matrix(3)

  def rotate(self, rads):
    """
    Add a rotation operation to the transformation matrix.
    :param rads: the amount to rotate (in radians)
    :return: self, for method chaining.
    """
    self._mtx = Transform2D.rotation_matrix(rads) * self._mtx
    return self

  def scale(self, xscale, yscale):
    """
    Add a scale operation to the transformation matrix.
    :param xscale: amount to scale in the x direction
    :param yscale: amount to scale in the y direction
    :return: self, for method chaining.
    """
    self._mtx = Transform2D.scaling_matrix(xscale, yscale) * self._mtx
    return self

  def shear(self, horizontal, vertical):
    """
    Add a shear operation to the transformation matrix.
    :param horizontal: amount of horizontal shear
    :param vertical: amount of vertical shearj
    :return: self, for method chaining
    """
    self._mtx = Transform2D.shearing_matrix(horizontal, vertical) * self._mtx
    return self

  def translate(self, dx, dy):
    """
    Add a translation operation to the transformation matrix.
    :param dx: Amount to translate in the x direction
    :param dy: Amount to translate in the y direction
    :return: self, for method chaining
    """
    self._mtx = Transform2D.translation_matrix(dx, dy) * self._mtx
    return self

  def reflect(self, line):
    """
    Add a reflection operation to the transformation matrix.
    :param line: the line over which a point should be reflected
    :return: self, for method chaining
    """
    self._mtx = Transform2D.reflection_matrix(line) * self._mtx
    return self

  def build(self) -> "Matrix":
    """
    :return: the compiled transformation matrix
    """
    return self._mtx.clone()

  def apply(self, pt: "Point2D") -> "Point2D":
    """
    :param pt: the point to which the transformation should be applied
    :return: the point after transformation
    """
    pmx = Matrix.from_point_with_padding(pt)
    return Point2D(*(self._mtx * pmx).as_list()[:2])
