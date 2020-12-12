from abc import ABC, abstractmethod


class GraphicsDelegate (ABC):
  
  @abstractmethod
  def draw_triangle(self, p1, p2, p3, color=None, line_color=None, line_width=1):
    pass
  
  @abstractmethod
  def show(self):
    pass
