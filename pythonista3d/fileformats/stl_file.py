import os
from enum import Enum
from pythonista3d.points import Point3D


class STLMode(Enum):
  """
  The two modes an STL file can exist in

  - ascii: the data of the file is stored in plaintext
  - binary: the data of the file is encoded in binary
  """
  ascii = 0
  binary = 1


class STLFacet(object):
  def __init__(self, normalstr: str):
    """
    Represents a single facet (made of three points and a normal vector) from the STL file.
    Initialize the facet with the normal, then add the points as they are parsed from the file.
    Assumes file is valid; does not perform file validation!
    :param normalstr: The string line from the STL file that contains the normal data to be parsed.
    """
    self.normal = Point3D(*[float(n) for n in normalstr.split()[-3:]])
    self.vs = []

  def add_vertex(self, vstr):
    """
    Add a vertex to the facet object
    :param vstr: the string containing the data from a vertex to be parsed and added to the facet object.
    """
    self.vs.append(Point3D(*[float(n) for n in vstr.split()[-3:]]))

  def __repr__(self):
    return "{}\n\t{}\n\t{}\n\t{}".format(self.normal, self.vs[0], self.vs[1], self.vs[2])


class STLFile(object):
  def __init__(self, path: str):
    """
    Represents an STL file and the data within.
    :param path: the path to the STL file.
    """
    self._path = path
    self._mode = None
    self._cur_line = 1
    self._cur_facet = None
    self._facets = []

  def load(self):
    """
    Parse the file and extract its data into the structure of this object.
    """
    if STLMode.ascii == self._mode:
      if not os.path.exists(self._path):
        raise Exception("File not found: [%s]" % self._path)
      with open(self._path) as f:
        ln = f.readline()
        while ln != '':
          line = ln.strip()
          self._process(line)

          # increment reader
          ln = f.readline()
          self._cur_line += 1
    if STLMode.binary == self._mode:
      raise Exception("Not implemented yet")

  def _process(self, line):
    """
    Parses a single line of the STL file in ascii mode and update this object's
    :param line: A single line of ascii text to parse
    :return:
    """
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
    """
    Print the data in this object for testing purposes.
    """
    for facet in self._facets:
      print(facet)