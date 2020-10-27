import os
from enum import Enum
from pythonista3d.points import Point3D


class STLMode(Enum):
  ascii = 0
  binary = 1


class STLFacet(object):
  def __init__(self, normalstr: str):
    self.normal = Point3D(*[float(n) for n in normalstr.split()[-3:]])
    self.vs = []

  def add_vertex(self, vstr):
    self.vs.append(Point3D(*[float(n) for n in vstr.split()[-3:]]))

  def __repr__(self):
    return "{}\n\t{}\n\t{}\n\t{}".format(self.normal, self.vs[0], self.vs[1], self.vs[2])


class STLFile(object):
  def __init__(self, path: str):
    print("Opening file: [%s]" % path)
    self._path = path
    self._mode = None
    self._cur_line = 1
    self._cur_facet = None
    self._facets = []

    self.load()

  def load(self):
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
        print(self._cur_facet)
        self._cur_facet = None
