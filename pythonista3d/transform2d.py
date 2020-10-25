
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point2D
from numbers import Number
from typing import SupportsFloat
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
  def rotation_matrix(rads: SupportsFloat = 0) -> "Matrix":
    """
    :param rads: the amount of desired rotation (in radians). Default: 0.
    :return: A matrix representing the desired rotation operation
    """
    return Matrix(3, 3, [math.cos(rads), -math.sin(rads), 0,
                         math.sin(rads), math.cos(rads), 0,
                         0, 0, 1])

  @staticmethod
  def rotate(pt: "Point2D", rads: SupportsFloat = 0) -> "Point2D":
    """
    Rotate a given point by the amount specified (in radians)
    :param pt: a 2D Point to rotate
    :param rads: the amount of desired rotation (in radians). Default: 0.
    :return: A point that has been rotated by the given amount
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.rotation_matrix(rads)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def scaling_matrix(x: Number = 1, y: Number = 1) -> "Matrix":
    """
    :param x: the amount of scaling in the x direction. Default: 1.
    :param y: the amount of scaling in the y direction. Default: 1.
    :return: A matrix representing the desired scale operation
    """
    return Matrix(3, 3, [x, 0, 0,
                         0, y, 0,
                         0, 0, 1])

  @staticmethod
  def scale(pt: "Point2D", x: Number = 1, y: Number = 1) -> "Point2D":
    """
    Scale a given point by the x_scale and y_scale amounts
    :param pt: a 2D Point to scale
    :param x: the amount of scaling in the x direction. Default 1.
    :param y: the amount of scaling in the y direction. Default 1.
    :return: A scaled point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.scaling_matrix(x, y)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def shearing_matrix(x: Number = 0, y: Number = 0) -> "Matrix":
    """
    :param x: The amount of horizontal shear
    :param y: The amount of vertical shear
    :return: A matrix representing the desired shearing operation
    """
    return Matrix(3, 3, [1, x, 0,
                         y, 1, 0,
                         0, 0, 1])

  @staticmethod
  def shear(pt: "Point2D", x: Number = 0, y: Number = 0) -> "Point2D":
    """
    Shear a given point by the horizontal and vertical amount specified
    :param pt: a 2D Point to shear
    :param x: The amount of horizontal shear. Default: 0.
    :param y: The amount of vertical shear. Default: 0.
    :return: A sheared point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform2D.shearing_matrix(x, y)
    return Point2D(*(tmx * pmx).as_list()[:2])

  @staticmethod
  def translation_matrix(dx: Number = 0, dy: Number = 0) -> "Matrix":
    """
    :param dx: change in the x direction. Default: 0.
    :param dy: change in the y direction. Default: 0.
    :return: A matrix representing the desired translation operation
    """
    return Matrix(3, 3, [1, 0, dx,
                         0, 1, dy,
                         0, 0, 1])

  @staticmethod
  def translate(pt: "Point2D", dx: Number = 0, dy: Number = 0) -> "Point2D":
    """
    Translate the given point by the x and y amounts specified
    :param pt: a 2D point to translate
    :param dx: change in the x direction. Default: 0.
    :param dy: change in the y direction. Default: 0.
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

  def rotate(self, rads: SupportsFloat = 0) -> "Transform2DBuilder":
    """
    Add a rotation operation to the transformation matrix.
    :param rads: the amount to rotate (in radians). Default: 0.
    :return: self, for method chaining.
    """
    self._mtx = Transform2D.rotation_matrix(rads) * self._mtx
    return self

  def scale(self, x: Number = 1, y: Number = 1) -> "Transform2DBuilder":
    """
    Add a scale operation to the transformation matrix.
    :param x: amount to scale in the x direction. Default: 1.
    :param y: amount to scale in the y direction. Default: 1.
    :return: self, for method chaining.
    """
    self._mtx = Transform2D.scaling_matrix(x, y) * self._mtx
    return self

  def shear(self, x: Number = 0, y: Number = 0) -> "Transform2DBuilder":
    """
    Add a shear operation to the transformation matrix.
    :param x: amount of horizontal shear. Default: 0.
    :param y: amount of vertical shear. Default: 0.
    :return: self, for method chaining
    """
    self._mtx = Transform2D.shearing_matrix(x, y) * self._mtx
    return self

  def translate(self, dx: Number = 0, dy: Number = 0) -> "Transform2DBuilder":
    """
    Add a translation operation to the transformation matrix.
    :param dx: Amount to translate in the x direction. Default: 0.
    :param dy: Amount to translate in the y direction Default: 0.
    :return: self, for method chaining
    """
    self._mtx = Transform2D.translation_matrix(dx, dy) * self._mtx
    return self

  def reflect(self, line: "ReflectionLine2D") -> "Transform2DBuilder":
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
