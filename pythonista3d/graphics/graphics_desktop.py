
from pythonista3d.graphics.graphics_delegate import GraphicsDelegate
from pythonista3d.points import Point2D


class GraphicsDesktop(GraphicsDelegate):
  """
  The graphics delegate specific to a Windows Desktop implementation
  """
  def __init__(self):
    pass

  def draw_triangle(self, p1: "Point2D", p2: "Point2D", p3: "Point2D", color=None, line_color=None, line_width=1):
    pass

  def show(self):
    pass

  def clear(self):
    pass
