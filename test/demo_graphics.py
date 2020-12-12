import test_context
from pythonista3d.graphics.graphics_factory import GraphicsFactory
from pythonista3d.points import Point2D, Point3D
from pythonista3d.fileformats.stl_file import STLFile, STLMode
from pythonista3d.scene3d import Scene3D
from pythonista3d.camera import Camera


d = GraphicsFactory.get_delegate()
d.show()

file = STLFile("rsc/cube_ascii.stl", STLMode.ascii)
file.load()

scn = Scene3D()
cam = Camera(
  pos=Point3D(0,0,2),
  look_dir=Point3D(0, 0, -1),
  up_dir=Point3D(0,1,0),
  n_dist=0.01,
  f_dist=5,
  fov=75)
scn.set_camera(cam)

d.draw_triangle(Point2D(100, 100), Point2D(300, 100), Point2D(100, 200), (1,1,1,0), '#fff')
