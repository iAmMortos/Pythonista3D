import test_context
from pythonista3d.graphics.graphics_factory import GraphicsFactory
from pythonista3d.points import Point2D, Point3D
from pythonista3d.vectors import Vector3D
from pythonista3d.fileformats.stl_file import STLFile, STLMode
from pythonista3d.scene3d import Scene3D
from pythonista3d.camera import Camera
from pythonista3d.transform3d import Transform3DBuilder, RotationAxis
from pythonista3d.matrix import Matrix
import math
import threading


d = GraphicsFactory.get_delegate()
d.show()

file = STLFile("rsc/cube_ascii.stl", STLMode.ascii)
file.load()

scn = Scene3D()
cam = Camera(
  pos=Point3D(0, -5, 0),
  look_dir=Vector3D(0, 1, 0),
  up_dir=Vector3D(0, 0, 1),
  n_dist=0.01,
  f_dist=10,
  fov=75)
scn.set_camera(cam)

tb = cam.get_std_view_volume_transformation()
rt = 0

def do_render():
  global rt
  d.clear()
  rtb = Transform3DBuilder().rotate(RotationAxis.z, rt)
  rt += math.pi/16
  rtb.build()
  rtb.add(tb)
  rtb.build()
  for ft in file.get_facets():
    np = ft.normal.as_point()
    np = rtb.apply(np)
    nv = Vector3D.from_point(np)
    print(nv.dot(cam.look_dir))
    if True or nv.dot(cam.look_dir) > 0:
      vs = []
      for p in ft.vs:
        p2 = rtb.apply(p)
        #p2 = tb.apply(p2)
        vs += [Point2D((p2.x + 1) / 2 * 736, (p2.y + 1) / 2 * 414)]
      d.draw_triangle(vs[0], vs[1], vs[2], (1,1,1,0), '#fff', 1)
  # threading.Timer(2, do_render).start()
  

do_render()
