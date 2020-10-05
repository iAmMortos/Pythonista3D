from __future__ import annotations

import math
from pythonista3d.errors import VectorSizeMismatchError
from pythonista3d.points import Point
from numbers import Number


class Vector(Point):
  def __init__(self, ndims: int, *vals: Number):
    super().__init__(ndims, *vals)

  def add(self, vec: Vector) -> Vector:
    if self.num_dimensions != vec.num_dimensions:
      raise VectorSizeMismatchError("Vertices must be the same dimensions to add. [%s] and [%s] provided." %
                                    (self.num_dimensions, vec.num_dimensions))
    return Vector(self.num_dimensions, *[self[i] + vec[i] for i in range(self.num_dimensions)])

  def subtract(self, vec: Vector) -> Vector:
    if self.num_dimensions != vec.num_dimensions:
      raise VectorSizeMismatchError("Vertices must be the same dimensions to subtract. [%s] and [%s] provided." %
                                    (self.num_dimensions, vec.num_dimensions))
    return Vector(self.num_dimensions, *[self[i] - vec[i] for i in range(self.num_dimensions)])

  def multiply(self, vec: Vector) -> Vector:
    if self.num_dimensions != vec.num_dimensions:
      raise VectorSizeMismatchError("Vertices must be the same dimensions to multiply. [%s] and [%s] provided." %
                                    (self.num_dimensions, vec.num_dimensions))
    return Vector(self.num_dimensions, *[self[i] * vec[i] for i in range(self.num_dimensions)])

  def add_const(self, const: Number) -> Vector:
    return Vector(self.num_dimensions, *[self[i] + const for i in range(self.num_dimensions)])

  def subtract_const(self, const: Number) -> Vector:
    return Vector(self.num_dimensions, *[self[i] - const for i in range(self.num_dimensions)])

  def scale(self, scalar: Number) -> Vector:
    return Vector(self.num_dimensions, *[self[i] * scalar for i in range(self.num_dimensions)])

  def normalize(self) -> Vector:
    m = self.get_magnitude()
    return Vector(self.num_dimensions, *[n / m for n in self._vals])

  def get_magnitude(self):
    return math.sqrt(sum([n ** 2 for n in self._vals]))


class Vector2D(Vector):
  def __init__(self, x: Number = 0, y: Number = 0):
    super().__init__(2, x, y)


class Vector3D(Vector):
  def __init__(self, x: Number = 0, y: Number = 0, z: Number = 0):
    super().__init__(3, x, y, z)
