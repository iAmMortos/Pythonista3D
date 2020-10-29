import test_context
import math
from pythonista3d.matrix import Matrix
from pythonista3d.points import Point3D
from pythonista3d.transform3d import Transform3D, Transform3DBuilder, RotationAxis, ReflectionPlane


def main():
  builder = Transform3DBuilder()
  builder.shear(yx=3, yz=-2)\
         .translate(-3, 10, 7)\
         .scale(3, 3, 3)\
         .rotate(RotationAxis.x, math.pi/4)\
         .reflect(ReflectionPlane.origin)
  mtx = builder.build()
  rmtx = builder.build_reverse()

  pt1 = Point3D(3, 1, 5)

  print("Original Point")
  print(pt1)

  print("Transformed Point")
  pt2 = builder.apply(pt1)
  print(pt2)

  print("Transformation Reversed")
  pt3 = builder.apply_reverse(pt2)
  print(pt3)

  m1 = Matrix(4, 4, [2, 5, 0, 8, 1, 4, 2, 6, 7, 8, 9, 3, 1, 5, 7, 8])

  print(m1)
  print(m1.inverse())
  print(m1 * m1.inverse())


if __name__ == '__main__':
  main()
