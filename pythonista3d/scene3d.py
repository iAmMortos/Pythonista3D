from pythonista3d.camera import Camera

# TODO: document and make API for easier use than demo test file


class Scene3D(object):
  def __init__(self):
    self.meshes = []
    self.camera = None
    
  def set_camera(self, camera):
    self.camera = camera

