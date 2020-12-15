from abc import ABC, abstractmethod
from pythonista3d.points import Point2D


class GraphicsDelegate (ABC):
  """
  An abstract interface for manipulating 3D graphics on a device.
  Currently only supports the VERY basic needs of this project: drawing triangles, clearing those triangles, and showing
  the graphics window.
  """
  
  @abstractmethod
  def draw_triangle(self, p1: "Point2D", p2: "Point2D", p3: "Point2D", color=None, line_color=None, line_width=1):
    """
    Draw a triangle defined by the 3 given
    :param p1: The first point of the triangle
    :param p2: The second point of the triangle
    :param p3: The third point of the triangle
    :param color: The fill color of the triangle. Can be made transparent with a 4th tuple value (1, 1, 1, 0)
    :param line_color: The color of the line. Can be transparent
    :param line_width: The width of the line
    """
    pass
  
  @abstractmethod
  def show(self):
    """
    Show the drawing surface
    """
    pass
    
  @abstractmethod
  def clear(self):
    """
    Clear the drawn triangles
    """
    pass
