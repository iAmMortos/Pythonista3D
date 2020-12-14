import test_context
from pythonista3d.vectors import Vector, Vector2D, Vector3D


def main():
  v3 = Vector3D(2, 5, 7)
  print(v3)
  print(-v3)
  print(type(v3), type(-v3))

  v2 = Vector2D(-5, 6)
  print(v2)
  print(-v2)
  print(type(v2), type(-v2))

  v6 = Vector(1, -2, 3, -4, 5, -6)
  print(v6)
  print(-v6)
  print(type(v6), type(-v6))

  va = Vector3D(1, 2, 3)
  vb = Vector3D(4, 5, 6)
  print(va)
  print(vb)
  print(va + vb)
  print(type(va), type(vb), type(va + vb))


if __name__ == '__main__':
  main()