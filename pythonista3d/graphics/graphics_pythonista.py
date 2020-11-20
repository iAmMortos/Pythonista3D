
from scene import *
from pythonista3d.graphics.pythonista_scene import PythonistaScene


from pythonista3d.graphics.graphics_delegate import GraphicsDelegate


class GraphicsPythonista (GraphicsDelegate):
  def __init__(self):
    self.scene = PythonistaScene()
    
  def draw_triangle(self, p1, p2, p3, color):
    pass

  def show(self):
    run(self.scene, show_fps=False)
