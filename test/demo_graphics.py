import test_context
from pythonista3d.graphics.graphics_factory import GraphicsFactory
from pythonista3d.points import Point2D, Point3D
from pythonista3d.vectors import Vector3D
from pythonista3d.fileformats.stl_file import STLFile, STLMode
from pythonista3d.scene3d import Scene3D
from pythonista3d.camera import Camera
from pythonista3d.transform3d import Transform3DBuilder
from pythonista3d.matrix import Matrix


d = GraphicsFactory.get_delegate()
d.show()

file = STLFile("rsc/teapot_ascii.stl", STLMode.ascii)
file.load()

scn = Scene3D()
cam = Camera(
  pos=Point3D(2, -3, 0),
  look_dir=Vector3D(-2, 3, 0),
  up_dir=Vector3D(0, 0, 1),
  n_dist=0.01,
  f_dist=10,
  fov=75)
scn.set_camera(cam)

tb = cam.get_std_view_volume_transformation()

for ft in file.get_facets():
  vs = []
  for p in ft.vs:
    p2 = tb.apply(p)
    vs += [Point2D((p2.x + 1) / 2 * 736, (p2.y + 1) / 2 * 414)]
  d.draw_triangle(vs[0], vs[1], vs[2], (1,1,1,0), '#fff', 1)
