import test_context
from pythonista3d.fileformats.stl_file import STLFile


def main():
  file = STLFile("rsc/cube_ascii.stl")
  file.load()
  file.print_facets()


if __name__ == '__main__':
  main()
