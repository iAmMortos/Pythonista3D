
from pythonista3d.fileformats.model_retriever import ModelRetriever
from pythonista3d.transform3d import Transform3DBuilder

# TODO: make editable mesh object instead of manually manipulating points


class Mesh(object):
  def __init__(self, model: "ModelRetriever"):
    self.facets = model.get_facets()

  def transform(self, tb: Transform3DBuilder):
    for facet in self.facets:
      facet.transform(tb)
