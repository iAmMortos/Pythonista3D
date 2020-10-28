import os
from enum import Enum
from pythonista3d.points import Point3D


class STLMode(Enum):
  """
  The different types of STL files.

  - ascii: human-readable, ascii data
  - binary: binary data
  """
  ascii = 0
  binary = 1


class STLFacet(object):
  """
  A single facet as defined by an STL file. Contains the three points in 3D space that make up this face, as well as the
  vector normal to this face.
  """
  def __init__(self, normalstr: str):
    self.normal = Point3D(*[float(n) for n in normalstr.split()[-3:]])
    self.vs = []

  def add_vertex(self, vstr: str):
    """
    Parse the given vertex string line from the STL file as a 3D Point, then add it to our short list of vertices.
    :param vstr: The string vertex line from the STL file to add to this facet definition
    """
    self.vs.append(Point3D(*[float(n) for n in vstr.split()[-3:]]))

  def __repr__(self):
    return "{}\n\t{}\n\t{}\n\t{}".format(self.normal, *self.vs)


class STLFile(object):
  """
  Represents an STL file and its data. Handles the file operations needed to read and interact with an STL file.
  """
  def __init__(self, path: str):
    self._path = path
    self._mode = None
    self._cur_line = 1
    self._cur_facet = None
    self._facets = []

    self.load()

  def load(self):
    """
    Load the STL file that exists at the path specified during creation of this object and parse its data.
    """
    if not os.path.exists(self._path):
      raise Exception("File not found: [%s]" % self._path)
    with open(self._path) as f:
      ln = f.readline()
      while ln != '':
        line = ln.strip()
        self.process(line)

        # increment reader
        ln = f.readline()
        self._cur_line += 1

  def process(self, line):
    if self._cur_line == 1:
      self._mode = STLMode.ascii if line.startswith("solid") else STLMode.binary
    else:
      if line.startswith("facet"):
        self._cur_facet = STLFacet(line)
      elif line.startswith("vertex"):
        self._cur_facet.add_vertex(line)
      elif line.startswith("endloop"):
        self._facets.append(self._cur_facet)
        self._cur_facet = None

  def print_facets(self):
    for facet in self._facets:
      print(facet)