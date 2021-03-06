import test_context
from pythonista3d.graphics.graphics_factory import GraphicsFactory
from pythonista3d.points import Point3D
from pythonista3d.vectors import Vector3D
from pythonista3d.fileformats.stl_file import STLFile, STLMode
from pythonista3d.scene3d import Scene3D
from pythonista3d.camera import Camera
from pythonista3d.mesh import Mesh


d = GraphicsFactory.get_delegate()
cam = Camera(
  pos=Point3D(0, -3, 0),
  look_dir=Vector3D(0, 3, 0),
  up_dir=Vector3D(0, 0, 1),
  n_dist=0.01,
  f_dist=10,
  fov=75)
scn = Scene3D(cam, d)

file = STLFile("rsc/sphere_ascii.stl", STLMode.ascii)
file.load()
obj = Mesh(file)

scn.add_mesh(obj)
scn.show()

scn.render()
