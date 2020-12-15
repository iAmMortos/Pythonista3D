
from abc import ABC, abstractmethod
from typing import List


class ModelReceiver(ABC):

  @abstractmethod
  def get_facets(self) -> List["Facet"]:
    pass
