
class Camera(object):
  def __init__(self, pos, look_dir, up_dir, n_dist, f_dist, fov):
    self._pos = pos
    self._look_dir = look_dir
    self._up_dir = up_dir
    self._near_plane_dist = n_dist
    self._far_plane_dist = f_dist
    self._field_of_view = fov

  @property
  def pos(self):
    return self._pos

  @pos.setter
  def pos(self, pos):
    self._pos = pos

  @property
  def look_dir(self):
    return self._look_dir

  @look_dir.setter
  def look_dir(self, look_dir):
    self._look_dir = look_dir
