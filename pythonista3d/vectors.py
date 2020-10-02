from __future__ import annotations

from pythonista3d.points import Point
from numbers import Number


class Vector(Point):
  def __init__(self, ndims: int, *vals: Number):
    super().__init__(ndims, *vals)

  def add(self, vec: Vector) -> Vector:
    pass

  def subtract(self, vec: Vector) -> Vector:
    pass

  def multiply(self, vec: Vector) -> Vector:
    pass

  def add_const(self, const: Number) -> Vector:
    pass

  def subtract_const(self, const: Number) -> Vector:
    pass

  def scale(self, scalar: Number) -> Vector:
    pass

  def normalize(self):
    pass


class Vector2D(Vector):
  def __init__(self, x=0, y=0):
    super().__init__(2, x, y)


class Vector3D(Vector):
  def __init__(self, x=0, y=0, z=0):
    super().__init__(3, x, y, z)
