
class MatrixIndexOutOfBoundsError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)


class MatrixSizeMismatchError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
