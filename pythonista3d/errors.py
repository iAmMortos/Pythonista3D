
class MatrixIndexOutOfBoundsError(Exception):
  def __init__(self, *args):
    super().__init__(*args)


class MatrixSizeMismatchError(Exception):
  def __init__(self, *args):
    super().__init__(*args)


class MatrixHasNoInverseError(Exception):
  def __init__(self, *args):
    super().__init__(*args)


class VectorSizeMismatchError(Exception):
  def __init__(self, *args):
    super().__init__(*args)
