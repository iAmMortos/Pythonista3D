import os
from enum import Enum
from pythonista3d.fileformats.model_retriever import ModelReceiver
from pythonista3d.points import Point3D
from pythonista3d.vectors import Vector3D
from pythonista3d.facet import Facet
from typing import List


class STLMode(Enum):
  """
  The two modes an STL file can exist in

  - ascii: the data of the file is stored in plaintext
  - binary: the data of the file is encoded in binary
  """
  ascii = 0
  binary = 1


class STLFacet(Facet):
  def __init__(self, normalstr: str):
    """
    Represents a single facet (made of three points and a normal vector) from the STL file.
    Initialize the facet with the normal, then add the points as they are parsed from the file.
    :param normalstr: The string line from the STL file that contains the normal data to be parsed.
    """
    self.normal = Vector3D(*[float(n) for n in normalstr.split()[-3:]])
    self.vertices = []

  def add_vertex(self, vstr: str):
    """
    Add a vertex to the facet object
    :param vstr: the string containing the data from a vertex to be parsed and added to the facet object.
    """
    self.vertices.append(Point3D(*[float(n) for n in vstr.split()[-3:]]))

  def __repr__(self):
    return "{}\n\t{}\n\t{}\n\t{}".format(self.normal, self.vertices[0], self.vertices[1], self.vertices[2])


class STLFile(ModelReceiver):
  def __init__(self, path: str, mode: 'STLMode'):
    """
    Represents an STL file and the data within.
    Assumes file is valid; does not perform file validation!
    :param path: the path to the STL file.
    """
    self._path = path
    self._mode = mode
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
    elif STLMode.binary == self._mode:
      raise Exception("Not implemented yet")
    else:
      raise Exception('No mode specified')
      
  def get_facets(self) -> List["STLFacet"]:
    """
    :return: the facets parsed from the file
    """
    return self._facets

  def _process(self, line: str):
    """
    Parses a single line of the STL file in ascii mode and update this object's
    :param line: A single line of ascii text to parse
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
