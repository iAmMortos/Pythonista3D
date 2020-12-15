
from pythonista3d.points import Point3D
from pythonista3d.vectors import Vector3D


class Facet(object):

  def __init__(self):
    self.vertices = []
    self.normal = Vector3D()

  def set_vertices(self, v1, v2, v3):
    self.vertices = [v1, v2, v3]
    self._recalc_normal()

  def transform(self, tb):
    self.vertices[0] = tb.apply(self.vertices[0])
    self.vertices[1] = tb.apply(self.vertices[1])
    self.vertices[2] = tb.apply(self.vertices[2])
    self._recalc_normal()

  def _recalc_normal(self):
    v1, v2, v3 = self.vertices
    self.normal = Vector3D.between_points(v2, v1).cross(Vector3D.between_points(v2, v3))
