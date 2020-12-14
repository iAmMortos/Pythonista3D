from scene import *
from pythonista3d.points import Point2D
import scene_drawing
import sound
import random
import math

A = Action


class PythonistaScene(Scene):
  def setup(self):
    self.nodes = []
    self.w, self.h = (100, 100)
    scene_drawing.fill(1, 0, 0)
    scene_drawing.stroke(1, 1, 1)
    scene_drawing.stroke_weight(2)

  def did_change_size(self):
    pass
    #self.w, self.h = self.size
    #print(self.w)

  def update(self):
    pass

  def touch_began(self, touch):
    pass

  def touch_moved(self, touch):
    pass

  def touch_ended(self, touch):
    pass
    
  def clear_triangles(self):
    for n in self.nodes:
      n.remove_from_parent()
    self.nodes = []
    
  @staticmethod
  def get_tri_center(a, b, c):
    xmin = min(a.x, b.x, c.x)
    xmax = max(a.x, b.x, c.x)
    ymin = min(a.y, b.y, c.y)
    ymax = max(a.y, b.y, c.y)
    cx = (xmax - xmin)/2 + xmin
    cy = (ymax - ymin)/2 + ymin
    return Point2D(cx,cy)
   
  def _cvpt(self, p):
    p.y *= -1
    return p
    
  def draw_triangle(self, p1, p2, p3, color=None, line_color=None, line_width=1):
    
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
    sn.position = sp
    self.nodes.append(sn)
    self.add_child(sn)


# if __name__ == '__main__':
#   run(Graphics(), show_fps=False)
