
class Camera(object):
  """
  Represents a perspective camera in 3D space
  """
  def __init__(self, pos, look_dir, up_dir, n_dist, f_dist, fov):
    """
    :param pos: The 3D position of the cameraj
    :param look_dir: The unit vector representing the direction the camera is looking
    :param up_dir: The unit vector representing the UP vector for the camera. Is normal to the camera's look vector.
    :param n_dist: The distance from the camera position to the near clipping plane
    :param f_dist: The distance from the camera position to the far clipping plane
    :param fov: The field of view
    """
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

  # TODO: finish accessors
