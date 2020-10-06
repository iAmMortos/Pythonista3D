
from pythonista3d.matrix import Matrix

def main():
  m = Matrix(2, 2, [4, -1, 0, 5])
  m2 = 2 * m
  print(m2)

if __name__ == '__main__':
  main()