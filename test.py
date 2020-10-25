
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point2D
from pythonista3d.transform2d import Transform2D, Transform2DBuilder, ReflectionLine2D

def main():
  print("Step-by-step transformation:")
  pt = Point2D(3, 1)
  print(pt)
  pt = Transform2D.shear(pt, 3, -2)
  print(pt)
  pt = Transform2D.translate(pt, -3, 10)
  print(pt)
  pt = Transform2D.scale(pt, 3, 3)
  print(pt)
  pt = Transform2D.rotate(pt, math.pi/2)
  print(pt)
  pt = Transform2D.reflect(pt, ReflectionLine2D.origin)
  print(pt)

  print("\nCombined transformation:")
  builder = Transform2DBuilder()
  builder.shear(3, -2)\
         .translate(-3, 10)\
         .scale(3, 3)\
         .rotate(math.pi / 2)\
         .reflect(ReflectionLine2D.origin)
  pt2 = Point2D(3, 1)
  print(pt2)
  print(builder.apply(pt2))
  
  print(builder.build())

if __name__ == '__main__':
  main()
