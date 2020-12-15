from pythonista3d.camera import Camera
from pythonista3d.mesh import Mesh
from pythonista3d.graphics.graphics_delegate import GraphicsDelegate
from pythonista3d.points import Point2D

# TODO: document and make API for easier use than demo test file


class Scene3D(object):
  def __init__(self, camera: Camera, gfx_delegate: GraphicsDelegate):
    self.meshes = []
    self.camera = camera
    self.gfx_delegate = gfx_delegate
    self.update_tb = None
    
  def add_mesh(self, mesh: Mesh):
    self.meshes.append(mesh)

  def show(self):
    self.gfx_delegate.show()

  def render(self):
    tb = self.camera.get_std_view_volume_transformation()
    tb.add(self.camera.get_unhinging_transformation())
    tb.build()
    self.gfx_delegate.clear()

    for mesh in self.meshes:
      self._render_mesh(mesh, tb)

  def _update(self):
    if self.update_tb is not None:
      for mesh in self.meshes:
        mesh.transform(self.update_tb)

  def _render_mesh(self, mesh: "Mesh", tb):
    for ft in mesh.facets:
      vs = []
      for p in ft.vertices:
        p2 = tb.apply(p)
        vs += [Point2D((p2.x + 1) / 2 * 736, (p2.y + 1) / 2 * 414)]
      self.gfx_delegate.draw_triangle(vs[0], vs[1], vs[2], (1, 1, 1, 0), '#fff', 1)
