
from pythonista3d.points import Point3D
from pythonista3d.vectors import Vector3D
from pythonista3d.points import Point
from pythonista3d.transform3d import Transform3DBuilder
from pythonista3d.matrix import Matrix
from numbers import Number
import math

class Camera(object):
  """
  Represents a perspective camera in 3D space
  """
  def __init__(self, pos: "Point3D", look_dir: "Vector3D", up_dir: "Vector3D", n_dist: "Number", f_dist: "Number", fov: "Number"):
    """
    :param pos: The 3D position of the camera
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
    self._aspect_ratio = 16 / 9
    self._hor_rads = self._field_of_view * math.pi / 180
    self._vert_rads = self._hor_rads / self._aspect_ratio

    # Order is important here
    self._w = self._calc_w()
    self._v = self._calc_v()
    self._u = self._calc_u()

    self._A = self._calc_A()
    self._B = self._calc_B()
    self._C = self._calc_C()

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
    self._recalc_uvw()

  @property
  def up_dir(self):
    return self._up_dir

  @up_dir.setter
  def up_dir(self, up_dir):
    self._up_dir = up_dir
    self._recalc_uvw()

  @property
  def w(self) -> "Vector3D":
    return self._w

  @property
  def v(self) -> "Vector3D":
    return self._v

  @property
  def u(self) -> "Vector3D":
    return self._u

  @property
  def A(self) -> "Point":
    return self._A

  @property
  def B(self) -> "Point":
    return self._B

  @property
  def C(self) -> "Point":
    return self._C

  def _calc_w(self):
    return -self._look_dir / self._look_dir.get_magnitude()

  def _calc_v(self):
    v = self._up_dir - self._up_dir.dot(self.w) * self.w
    return v / v.get_magnitude()

  def _calc_u(self):
    return self.v.cross(self.w)

  def _calc_A(self) -> "Point":
    return self.w.scale(self._far_plane_dist) - self.pos

  def _calc_B(self) -> "Point":
    return self.u.scale(self._far_plane_dist * math.tan(self._hor_rads / 2)) + self.A

  def _calc_C(self) -> "Point":
    # return self.v.scale(self._far_plane_dist) + self.A
    return self.v.scale(self._far_plane_dist * math.tan(self._vert_rads / 2)) - self.w.scale(self._far_plane_dist) + self.pos

  def _recalc_uvw(self):
    self._w = self._calc_w()
    self._v = self._calc_v()
    self._u = self._calc_u()

  def get_std_view_volume_transformation(self):
    tb = Transform3DBuilder()
    tb.translate(-self.pos.x, -self.pos.y, -self.pos.z)\
      .custom(Matrix(4, 4, [self.u.x, self.u.y, self.u.z, 0,
                            self.v.x, self.v.y, self.v.z, 0,
                            self.w.x, self.w.y, self.w.z, 0,
                            0, 0, 0, 1]))\
      .scale(1 / (self._far_plane_dist * math.tan(self._hor_rads / 2)),
             1 / (self._far_plane_dist * math.tan(self._vert_rads / 2)),
             1 / self._far_plane_dist)\
      .build()
    return tb

  def get_unhinging_transformation(self):
    f = self._far_plane_dist
    n = self._near_plane_dist
    fn = f - n
    c = -n / f
    tb = Transform3DBuilder()
    tb.custom(Matrix(4, 4, [fn,  0,   0, 0,
                            0,  fn,   0, 0,
                            0,   0,   f, n,
                            0,   0, -fn, 0]))
    tb.build()
    return tb

  # TODO: finish accessors
