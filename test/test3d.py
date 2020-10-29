import test_context 
import math
from pythonista3d.matrix import Matrix
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
  mtx = builder.build()
  rmtx = builder.build_reverse()
  pt2 = Point3D(3, 1, 5)
  print(pt2)
  pt3 = builder.apply(pt2)
  print(pt3)
  print(builder.apply_reverse(pt3))
  print('\n\n')
  print('Transformation matrix:\n%s' % mtx)
  print('Reverse Transformation matrix:\n%s' % rmtx)
  imtx = mtx.inverse()
  print('Inverse:\n%s' % imtx)
  print((imtx * Matrix.from_point_with_padding(pt3)).as_list()[:3])


if __name__ == '__main__':
  main()
