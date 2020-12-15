
from pythonista3d.points import Point3D
from pythonista3d.vectors import Vector3D


class Facet(object):

  def __init__(self):
    self.vertices = []
    self.normal = Vector3D()
