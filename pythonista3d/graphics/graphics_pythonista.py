
from scene import *
from pythonista3d.graphics.pythonista_scene import PythonistaScene
from pythonista3d.graphics.graphics_delegate import GraphicsDelegate
from pythonista3d.points import Point2D


class GraphicsPythonista (GraphicsDelegate):
  """
  The graphics delegate specific to Pythonista
  """

  def __init__(self):
    self.scene = PythonistaScene()
    
  def draw_triangle(self, p1: "Point2D", p2: "Point2D", p3: "Point2D", color=None, line_color=None, line_width=1):
    self.scene.draw_triangle(p1, p2, p3, color, line_color, line_width)

  def show(self):
    run(self.scene, show_fps=False)
  
  def clear(self):
    self.scene.clear_triangles()
