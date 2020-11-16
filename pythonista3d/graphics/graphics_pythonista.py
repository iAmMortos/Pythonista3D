from scene import *
import sound
import random
import math
A = Action

class Graphics (Scene):
  def __init__(self):
    print('hey oo')
    
  def setup(self):
    pass
  
  def did_change_size(self):
    pass
  
  def update(self):
    pass
  
  def touch_began(self, touch):
    pass
  
  def touch_moved(self, touch):
    pass
  
  def touch_ended(self, touch):
    pass

if __name__ == '__main__':
  run(Graphics(), show_fps=False)
