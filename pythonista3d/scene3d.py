from pythonista3d.camera import Camera


class Scene3D(object):
  def __init__(self):
    self.meshes = []
    self.camera = None
    
  def set_camera(self, camera):
    self.camera = camera

