import test_context
from pythonista3d.fileformats.stl_file import STLFile, STLMode


def main():
  file = STLFile("rsc/cube_ascii.stl", STLMode.ascii)
  file.load()
  fs = file.get_facets()
  for f in fs:
    print(f.vs)
    print(f.normal)


if __name__ == '__main__':
  main()
