from scene import *
from pythonista3d.points import Point2D
import scene_drawing
import sound
import random
import math


A = Action


class PythonistaScene(Scene):
  """
  The Pythonista-side scene object that actually does the drawing to screen.
  """
  def setup(self):
    """
    Built-in method of a Scene object from Pythonista
    """
    self.nodes = []
    self.w, self.h = (100, 100)
    scene_drawing.fill(1, 0, 0)
    scene_drawing.stroke(1, 1, 1)
    scene_drawing.stroke_weight(2)

  def did_change_size(self):
    """
    Built-in method of a Scene object from Pythonista
    """
    pass

  def update(self):
    """
    Built-in method of a Scene object from Pythonista
    """
    pass

  def touch_began(self, touch):
    """
    Built-in method of a Scene object from Pythonista
    """
    pass

  def touch_moved(self, touch):
    """
    Built-in method of a Scene object from Pythonista
    """
    pass

  def touch_ended(self, touch):
    """
    Built-in method of a Scene object from Pythonista
    """
    pass
    
  def clear_triangles(self):
    """
    Remove all triangles from the screen
    TODO: create some kind of NodePool so the nodes can be reused instead of deleted and recreated every time.
          this would help to improve performance.j
    """
    for n in self.nodes:
      n.remove_from_parent()
    self.nodes = []
    
  @staticmethod
  def get_tri_center(a: "Point2D", b: "Point2D", c: "Point2D"):
    """
    Since the coordinates used to create a path are completely separate from the position of the ShapeNode housing the
    path, this convenience method provides the coordinate to which the ShapeNode must be positioned so the path ends up
    where it should be on the screen.
    :param a: The first point
    :param b: The second point
    :param c: The third point
    :return: the center of the bounding box that surrounds the three given points.
    """
    xmin = min(a.x, b.x, c.x)
    xmax = max(a.x, b.x, c.x)
    ymin = min(a.y, b.y, c.y)
    ymax = max(a.y, b.y, c.y)
    cx = (xmax - xmin)/2 + xmin
    cy = (ymax - ymin)/2 + ymin
    return Point2D(cx, cy)
   
  def _cvpt(self, p: "Point2D"):
    """
    Convert the given point from the Pythonista coordinate system (where 0,0 is the top left corner of the screen) to
    the standard coordinate system (where 0,0 is the bottom left corner of the screen.
    :param p: The point to convert
    :return: The converted point in the standard 2D coordinate system.
    """
    p.y *= -1
    return p
    
  def draw_triangle(self, p1: "Point2D", p2: "Point2D", p3: "Point2D", color=None, line_color=None, line_width=1):
    """
    Draw a triangle made up of the three given points with the colors and line width specified.
    :param p1: First point
    :param p2: Second point
    :param p3: Third point
    :param color: triangle fill color
    :param line_color: triangle line color
    :param line_width: triangle line width
    """
    
    sp = self.get_tri_center(p1, p2, p3)
    
    p1 = self._cvpt(p1)
    p2 = self._cvpt(p2)
    p3 = self._cvpt(p3)
    
    p = ui.Path()
    p.move_to(p1.x, p1.y)
    p.line_to(p2.x, p2.y)
    p.line_to(p3.x, p3.y)
    p.close()
      
    sn = ShapeNode(p, color, line_color)
    # The ShapeNode object must be moved so it actually ends up where the given points would dictate.
    sn.position = sp
    self.nodes.append(sn)
    self.add_child(sn)
