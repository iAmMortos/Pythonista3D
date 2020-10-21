
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point3D
from numbers import Number
from typing import SupportsFloat
from enum import Enum


class ReflectionLine3D(Enum):
  """
  Represents the different planes of reflection in 3D space
  """
  origin = "origin"
  xy = "xy"
  yz = "yz"
  zx = "zx"


class RotationAxis(Enum):
  x = "x"
  y = "y"
  z = "z"


class Transform3D(object):
  """
  Contains the means of translating things in 3 dimensions using matrix math.
  Can perform transformations on individual points, or can provide the appropriate matrix by which
  the transformation can be performed
  """

  @staticmethod
  def rotation_matrix(axis: "RotationAxis", rads: SupportsFloat) -> "Matrix":
    """
    :param axis: the axis around which to perform the rotation
    :param rads: the amount of desired rotation (in radians)
    :return: A matrix representing the desired rotation operation
    """
    m = None
    if RotationAxis.x == axis:
      m = Matrix(4, 4, [1, 0, 0, 0,
                        0, math.cos(rads), -math.sin(rads), 0,
                        0, math.sin(rads), math.cos(rads), 0,
                        0, 0, 0, 1])
    elif RotationAxis.y == axis:
      m = Matrix(4, 4, [math.cos(rads), 0, math.sin(rads), 0,
                        0, 1, 0, 0,
                        -math.sin(rads), 0, math.cos(rads), 0,
                        0, 0, 0, 1])
    elif RotationAxis.z == axis:
      m = Matrix(4, 4, [math.cos(rads), -math.sin(rads), 0, 0,
                        math.sin(rads), math.cos(rads), 0, 0,
                        0, 0, 1, 0,
                        0, 0, 0, 1])
    return m

  @staticmethod
  def rotate(pt: "Point3D", axis: "RotationAxis", rads: SupportsFloat) -> "Point3D":
    """
    Rotate a given point by the amount specified (in radians)
    :param pt: a 2D Point to rotate
    :param axis: the axis around which to perform the rotation
    :param rads: the amount of desired rotation (in radians)j
    :return: A point that has been rotated by the given amount
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.rotation_matrix(axis, rads)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def scaling_matrix(x_scale: Number, y_scale: Number, z_scale: Number) -> "Matrix":
    """
    :param x_scale: the amount of scaling in the x direction
    :param y_scale: the amount of scaling in the y direction
    :param z_scale: the amount of scaling in the z direction
    :return: A matrix representing the desired scale operation
    """
    return Matrix(4, 4, [x_scale, 0, 0, 0,
                         0, y_scale, 0, 0,
                         0, 0, z_scale, 0,
                         0, 0, 0, 1])

  @staticmethod
  def scale(pt: "Point3D", x_scale: Number, y_scale: Number, z_scale: Number) -> "Point3D":
    """
    Scale a given point by the x_scale and y_scale amounts
    :param pt: a 2D Point to scale
    :param x_scale: the amount of scaling in the x direction
    :param y_scale: the amount of scaling in the y direction
    :param z_scale: the amount of scaling in the z direction
    :return: A scaled point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.scaling_matrix(x_scale, y_scale, z_scale)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def shearing_matrix(xy: Number = 0, xz: Number = 0,
                      yx: Number = 0, yz: Number = 0,
                      zx: Number = 0, zy: Number = 0) -> "Matrix":
    """
    :parameter xy: amount of shearing on x values in the y direction
    :parameter xz: amount of shearing on x values in the z direction
    :parameter yx: amount of shearing on y values in the x direction
    :parameter yz: amount of shearing on y values in the z direction
    :parameter zx: amount of shearing on z values in the x direction
    :parameter zy: amount of shearing on z values in the y direction
    :return: A matrix representing the desired shearing operation
    """
    return Matrix(4, 4, [1, yx, zx, 0,
                         xy, 1, zy, 0,
                         xz, yz, 1, 0,
                         0, 0, 0, 1])

  @staticmethod
  def shear(pt: "Point3D",
            xy: Number = 0, xz: Number = 0,
            yx: Number = 0, yz: Number = 0,
            zx: Number = 0, zy: Number = 0) -> "Point3D":
    """
    Shear a given point by the horizontal and vertical amount specified
    :param pt: a 2D Point to shear
    :parameter xy: amount of shearing on x values in the y direction
    :parameter xz: amount of shearing on x values in the z direction
    :parameter yx: amount of shearing on y values in the x direction
    :parameter yz: amount of shearing on y values in the z direction
    :parameter zy: amount of shearing on z values in the y direction
    :parameter zx: amount of shearing on z values in the x direction
    :return: A sheared point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.shearing_matrix(xy, xz, yx, yz, zx, zy)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def translation_matrix(dx: Number, dy: Number, dz: Number) -> "Matrix":
    """
    :param dx: change in the x direction
    :param dy: change in the y direction
    :param dz: change in the z direction
    :return: A matrix representing the desired translation operation
    """
    return Matrix(4, 4, [1, 0, 0, dx,
                         0, 1, 0, dy,
                         0, 0, 1, dz,
                         0, 0, 0, 1])

  @staticmethod
  def translate(pt: "Point3D", dx: Number, dy: Number, dz: Number) -> "Point3D":
    """
    Translate the given point by the x and y amounts specified
    :param pt: a 2D point to translate
    :param dx: change in the x direction
    :param dy: change in the y direction
    :param dz: change in the z direction
    :return: A translated point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.translation_matrix(dx, dy, dz)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def reflection_matrix(plane: "ReflectionLine3D") -> Matrix:
    """
    :param plane: the plane over which the reflection should be performed
    :return: A matrix representing the desired reflection operation
    """
    d = {ReflectionLine3D.xy: [1, 0, 0, 0,
                               0, 1, 0, 0,
                               0, 0, -1, 0,
                               0, 0, 0, 1],
         ReflectionLine3D.yz: [-1, 0, 0, 0,
                               0, 1, 0, 0,
                               0, 0, 1, 0,
                               0, 0, 0, 1],
         ReflectionLine3D.zx: [1, 0, 0, 0,
                               0, -1, 0, 0,
                               0, 0, 1, 0,
                               0, 0, 0, 1],
         ReflectionLine3D.origin: [-1, 0, 0, 0,
                                   0, -1, 0, 0,
                                   0, 0, -1, 0,
                                   0, 0, 0, 1]}
    return Matrix(4, 4, d[plane])

  @staticmethod
  def reflect(pt: "Point3D", line: "ReflectionLine3D") -> "Point3D":
    """
    Reflect the given point over the specified reflection line
    :param pt: a 2D point to reflect
    :param line: a ReflectionLine2D value specifying the line of reflection
    :return: A reflected point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.reflection_matrix(line)
    return Point3D(*(tmx * pmx).as_list()[:3])


class Transform3DBuilder(object):
  def __init__(self):
    """
    Composites multiple transformations into a single transformation matrix for efficiency of computation.
    Can produce the actual finished matrix, or apply the matrix to a given 2D point.
    """
    self._mtx = Matrix.identity_matrix(4)

  def rotate(self, axis, rads):
    """
    Add a rotation operation to the transformation matrix.
    :param axis:
    :param rads: the amount to rotate (in radians)
    :return: self, for method chaining.
    """
    self._mtx = Transform3D.rotation_matrix(axis, rads) * self._mtx
    return self

  def scale(self, x_scale, y_scale, z_scale):
    """
    Add a scale operation to the transformation matrix.
    :param x_scale: amount to scale in the x direction
    :param y_scale: amount to scale in the y direction
    :param z_scale:
    :return: self, for method chaining.
    """
    self._mtx = Transform3D.scaling_matrix(x_scale, y_scale, z_scale) * self._mtx
    return self

  def shear(self, xy, xz, yx, yz, zx, zy):
    """
    Add a shear operation to the transformation matrix.
    :param xy:
    :param xz:
    :param yx:
    :param yz:
    :param zx:
    :param zy:
    :return: self, for method chaining
    """
    self._mtx = Transform3D.shearing_matrix(xy, xz, yx, yz, zx, zy) * self._mtx
    return self

  def translate(self, dx, dy, dz):
    """
    Add a translation operation to the transformation matrix.
    :param dx: Amount to translate in the x direction
    :param dy: Amount to translate in the y direction
    :param dz: Amount to translate in the z direction
    :return: self, for method chaining
    """
    self._mtx = Transform3D.translation_matrix(dx, dy, dz) * self._mtx
    return self

  def reflect(self, plane):
    """
    Add a reflection operation to the transformation matrix.
    :param plane: the plane over which a point should be reflected
    :return: self, for method chaining
    """
    self._mtx = Transform3D.reflection_matrix(plane) * self._mtx
    return self

  def build(self) -> "Matrix":
    """
    :return: the compiled transformation matrix
    """
    return self._mtx.clone()

  def apply(self, pt: "Point3D") -> "Point3D":
    """
    :param pt: the point to which the transformation should be applied
    :return: the point after transformation
    """
    pmx = Matrix.from_point_with_padding(pt)
    return Point3D(*(self._mtx * pmx).as_list()[:3])
