
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point3D
from numbers import Number
from typing import SupportsFloat
from enum import Enum


class ReflectionPlane(Enum):
  """
  Represents the different planes of reflection in 3D space

  - xy: Reflects all points over the xy plane
  - yz: Reflects all points over the yz plane
  - zx: Reflects all points over the zx plane
  - origin: Reflects all points over the origin
  """
  xy = "xy"
  yz = "yz"
  zx = "zx"
  origin = "origin"


class RotationAxis(Enum):
  """
  Represents the 3D axes around which rotation can occur

  - x: Rotates all points around the x axis
  - y: Rotates all points around the y axis
  - z: Rotates all points around the z axis
  """
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
  def rotation_matrix(axis: "RotationAxis", rads: SupportsFloat = 0) -> "Matrix":
    """
    :param axis: the axis around which to perform the rotation
    :param rads: the amount of desired rotation (in radians). Default: 0.
    :return: A matrix representing the desired rotation operation
    """
    m = None
    c = math.cos(rads)
    s = math.sin(rads)
    if RotationAxis.x == axis:
      m = Matrix(4, 4, [1, 0, 0, 0,
                        0, c, -s, 0,
                        0, s, c, 0,
                        0, 0, 0, 1])
    elif RotationAxis.y == axis:
      m = Matrix(4, 4, [c, 0, s, 0,
                        0, 1, 0, 0,
                        -s, 0, c, 0,
                        0, 0, 0, 1])
    elif RotationAxis.z == axis:
      m = Matrix(4, 4, [c, -s, 0, 0,
                        s, c, 0, 0,
                        0, 0, 1, 0,
                        0, 0, 0, 1])
    return m

  @staticmethod
  def rotate(pt: "Point3D", axis: "RotationAxis", rads: SupportsFloat = 0) -> "Point3D":
    """
    Rotate a given point by the amount specified (in radians)
    :param pt: a 3D Point to rotate
    :param axis: the axis around which to perform the rotation
    :param rads: the amount of desired rotation (in radians). Default: 0.
    :return: A point that has been rotated by the given amount
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.rotation_matrix(axis, rads)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def scaling_matrix(x: Number = 1, y: Number = 1, z: Number = 1) -> "Matrix":
    """
    :param x: the amount of scaling in the x direction. Default: 1.
    :param y: the amount of scaling in the y direction. Default: 1.
    :param z: the amount of scaling in the z direction. Default: 1.
    :return: A matrix representing the desired scale operation
    """
    return Matrix(4, 4, [x, 0, 0, 0,
                         0, y, 0, 0,
                         0, 0, z, 0,
                         0, 0, 0, 1])

  @staticmethod
  def scale(pt: "Point3D", x: Number = 1, y: Number = 1, z: Number = 1) -> "Point3D":
    """
    Scale a given point by the x, y, and z amounts
    :param pt: a 3D Point to scale
    :param x: the amount of scaling in the x direction. Default: 1.
    :param y: the amount of scaling in the y direction. Default: 1.
    :param z: the amount of scaling in the z direction. Default: 1.
    :return: A scaled point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.scaling_matrix(x, y, z)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def shearing_matrix(xy: Number = 0, xz: Number = 0,
                      yx: Number = 0, yz: Number = 0,
                      zx: Number = 0, zy: Number = 0) -> "Matrix":
    """
    :parameter xy: amount of shearing on x values in the y direction. Default: 0.
    :parameter xz: amount of shearing on x values in the z direction. Default: 0.
    :parameter yx: amount of shearing on y values in the x direction. Default: 0.
    :parameter yz: amount of shearing on y values in the z direction. Default: 0.
    :parameter zx: amount of shearing on z values in the x direction. Default: 0.
    :parameter zy: amount of shearing on z values in the y direction. Default: 0.
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
    Shear a given point by the amounts specified
    :param pt: a 3D Point to shear. Default: 0.
    :parameter xy: amount of shearing on x values in the y direction. Default: 0.
    :parameter xz: amount of shearing on x values in the z direction. Default: 0.
    :parameter yx: amount of shearing on y values in the x direction. Default: 0.
    :parameter yz: amount of shearing on y values in the z direction. Default: 0.
    :parameter zy: amount of shearing on z values in the y direction. Default: 0.
    :parameter zx: amount of shearing on z values in the x direction. Default: 0.
    :return: A sheared point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.shearing_matrix(xy, xz, yx, yz, zx, zy)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def translation_matrix(dx: Number = 0, dy: Number = 0, dz: Number = 0) -> "Matrix":
    """
    :param dx: change in the x direction. Default: 0.
    :param dy: change in the y direction. Default: 0.
    :param dz: change in the z direction. Default: 0.
    :return: A matrix representing the desired translation operation
    """
    return Matrix(4, 4, [1, 0, 0, dx,
                         0, 1, 0, dy,
                         0, 0, 1, dz,
                         0, 0, 0, 1])

  @staticmethod
  def translate(pt: "Point3D", dx: Number = 0, dy: Number = 0, dz: Number = 0) -> "Point3D":
    """
    Translate the given point by the x and y amounts specified
    :param pt: a 3D point to translate
    :param dx: change in the x direction. Default: 0.
    :param dy: change in the y direction. Default: 0.
    :param dz: change in the z direction. Default: 0.
    :return: A translated point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.translation_matrix(dx, dy, dz)
    return Point3D(*(tmx * pmx).as_list()[:3])

  @staticmethod
  def reflection_matrix(plane: "ReflectionPlane") -> Matrix:
    """
    :param plane: the plane over which the reflection should be performed
    :return: A matrix representing the desired reflection operation
    """
    d = {ReflectionPlane.xy: [1, 0, 0, 0,
                              0, 1, 0, 0,
                              0, 0, -1, 0,
                              0, 0, 0, 1],
         ReflectionPlane.yz: [-1, 0, 0, 0,
                              0, 1, 0, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 1],
         ReflectionPlane.zx: [1, 0, 0, 0,
                              0, -1, 0, 0,
                              0, 0, 1, 0,
                              0, 0, 0, 1],
         ReflectionPlane.origin: [-1, 0, 0, 0,
                                  0, -1, 0, 0,
                                  0, 0, -1, 0,
                                  0, 0, 0, 1]}
    return Matrix(4, 4, d[plane])

  @staticmethod
  def reflect(pt: "Point3D", plane: "ReflectionPlane") -> "Point3D":
    """
    Reflect the given point over the specified reflection plane
    :param pt: a 3D point to reflect
    :param plane: a ReflectionPlane3D value specifying the plane of reflection in 3D space.
    :return: A reflected point
    """
    pmx = Matrix.from_point_with_padding(pt)
    tmx = Transform3D.reflection_matrix(plane)
    return Point3D(*(tmx * pmx).as_list()[:3])


class Transform3DBuilder(object):
  def __init__(self):
    """
    Composites multiple transformations into a single transformation matrix for efficiency of computation.
    Can produce the actual finished matrix, or apply the matrix to a given 3D point.
    """
    self._mtx = Matrix.identity_matrix(4)

  def rotate(self, axis, rads: SupportsFloat = 0) -> "Transform3DBuilder":
    """
    Add a rotation operation to the transformation matrix.
    :param axis:
    :param rads: the amount to rotate (in radians). Default: 0.
    :return: self, for method chaining.
    """
    self._mtx = Transform3D.rotation_matrix(axis, rads) * self._mtx
    return self

  def scale(self, x: Number = 1, y: Number = 1, z: Number = 1) -> "Transform3DBuilder":
    """
    Add a scale operation to the transformation matrix.
    :param x: amount to scale in the x direction. Default: 1.
    :param y: amount to scale in the y direction. Default: 1.
    :param z: amount to scale in the z direction. Default: 1.
    :return: self, for method chaining.
    """
    self._mtx = Transform3D.scaling_matrix(x, y, z) * self._mtx
    return self

  def shear(self,
            xy: Number = 0, xz: Number = 0,
            yx: Number = 0, yz: Number = 0,
            zx: Number = 0, zy: Number = 0) -> "Transform3DBuilder":
    """
    Add a shear operation to the transformation matrix.
    :param xy: The amount to shear the x points in the y direction. Default: 0.
    :param xz: The amount to shear the x points in the z direction. Default: 0.
    :param yx: The amount to shear the y points in the x direction. Default: 0.
    :param yz: The amount to shear the y points in the z direction. Default: 0.
    :param zx: The amount to shear the z points in the x direction. Default: 0.
    :param zy: The amount to shear the z points in the y direction. Default: 0.
    :return: self, for method chaining
    """
    self._mtx = Transform3D.shearing_matrix(xy, xz, yx, yz, zx, zy) * self._mtx
    return self

  def translate(self, dx: Number = 0, dy: Number = 0, dz: Number = 0) -> "Transform3DBuilder":
    """
    Add a translation operation to the transformation matrix.
    :param dx: Amount to translate in the x direction. Default: 0.
    :param dy: Amount to translate in the y direction. Default: 0.
    :param dz: Amount to translate in the z direction. Default: 0.
    :return: self, for method chaining
    """
    self._mtx = Transform3D.translation_matrix(dx, dy, dz) * self._mtx
    return self

  def reflect(self, plane) -> "Transform3DBuilder":
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
