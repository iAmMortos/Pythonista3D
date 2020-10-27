
import math
from pythonista3d.points import Point3D
from pythonista3d.transform3d import Transform3D, Transform3DBuilder, RotationAxis, ReflectionPlane


def main():
  print("Step-by-step transformation:")
  pt = Point3D(3, 1, 5)
  print(pt)
  pt = Transform3D.shear(pt, yx=3, yz=-2)
  print(pt)
  pt = Transform3D.translate(pt, -3, 10, 7)
  print(pt)
  pt = Transform3D.scale(pt, 3, 3, 3)
  print(pt)
  pt = Transform3D.rotate(pt, RotationAxis.x, math.pi/4)
  print(pt)
  pt = Transform3D.reflect(pt, ReflectionPlane.origin)
  print(pt)

  print("\nCombined transformation:")
  builder = Transform3DBuilder()
  builder.shear(yx=3, yz=-2)\
         .translate(-3, 10, 7)\
         .scale(3, 3, 3)\
         .rotate(RotationAxis.x, math.pi/4)\
         .reflect(ReflectionPlane.origin)
  pt2 = Point3D(3, 1, 5)
  print(pt2)
  print(builder.apply(pt2))


if __name__ == '__main__':
  main()
