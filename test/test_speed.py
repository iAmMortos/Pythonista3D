import test_context
import random
import math
from pythonista3d.points import Point3D
from pythonista3d.transform3d import Transform3DBuilder, RotationAxis
from datetime import datetime


def test_with_objects(pts, tb):
  tstart = datetime.now().timestamp()
  transformed = [tb.apply(p) for p in pts]
  print("Done transforming all points: %s" % (datetime.now().timestamp() - tstart))
  print(transformed[:10])


def test_with_primitives(pts, tb):
  ml = tb.build().as_list()
  newlist = []
  for pt in pts:
    newlist.append(pt.x)
    newlist.append(pt.y)
    newlist.append(pt.z)

  def mult(m, p1, p2, p3):
    return (m[0] * p1 + m[1] * p2 + m[2] * p3 + m[3],
            m[4] * p1 + m[5] * p2 + m[6] * p3 + m[7],
            m[8] * p1 + m[9] * p2 + m[10] * p3 + m[11])

  transformedlist = []
  tstart = datetime.now().timestamp()
  for i in range(0, len(newlist), 3):
    transformedlist.append(mult(ml, newlist[i], newlist[i+1], newlist[i+2]))
  print("Done transforming all points: %s" % (datetime.now().timestamp() - tstart))
  print(transformedlist[:10])



def main():
  tb = Transform3DBuilder().rotate(RotationAxis.y, math.pi / 4)
  pts = []
  for _ in range(100000):
    pts.append(Point3D(random.random(), random.random(), random.random()))

  test_with_objects(pts, tb)
  test_with_primitives(pts, tb)


if __name__ == '__main__':
  main()
