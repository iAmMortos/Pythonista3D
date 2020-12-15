
from pythonista3d.facet import Facet

from abc import ABC, abstractmethod
from typing import List


class ModelRetriever(ABC):
  """
  An abstract class for API purposes. Anything that implements the get_facets method.
  """

  @abstractmethod
  def get_facets(self) -> List["Facet"]:
    """
    Return the list of facets in this model
    :return:
    """
    pass
