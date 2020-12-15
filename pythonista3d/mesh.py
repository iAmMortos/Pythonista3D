
from pythonista3d.fileformats.model_retriever import ModelReceiver

# TODO: make editable mesh object instead of manually manipulating points


class Mesh(object):
  def __init__(self, model: "ModelReceiver"):
    self.facets = model.get_facets()
