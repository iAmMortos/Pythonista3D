from abc import ABC, abstractmethod

class GraphicsDelegate (ABC):
  
  @abstractmethod
  def draw_triangle(self, p1, p2, p3, color):
    pass
  
  @abstractmethod
  def show(self):
    pass
