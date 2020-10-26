
import random
import math
from pythonista3d.points import Point3D
from pythonista3d.transform3d import Transform3DBuilder, RotationAxis
from datetime import datetime


def main():
  pts = []
  tb = Transform3DBuilder().rotate(RotationAxis.y, math.pi / 4)
  tstart = datetime.now().timestamp()
  print("Generating random 3D points.")
  for _ in range(100000):
    pts.append(Point3D(random.random(), random.random(), random.random()))
  print("Done creating points: %s" % (datetime.now().timestamp() - tstart))

  tstart = datetime.now().timestamp()
  [tb.apply(p) for p in pts]
  print("Done transforming all points: %s" % (datetime.now().timestamp() - tstart))


if __name__ == '__main__':
  main()