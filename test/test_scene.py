import test_context

from pythonista3d.scene3d import Scene3D
from pythonista3d.camera import Camera
from pythonista3d.graphics.graphics_factory import GraphicsFactory


def main():
  d = GraphicsFactory.get_delegate()
  d.show()

if __name__ == '__main__':
  main()
