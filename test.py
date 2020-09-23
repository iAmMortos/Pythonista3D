
from libs.matrix import Matrix

def main():
  m1 = Matrix(1, 3, [1, 2, 3])
  m2 = Matrix(3, 1, [4, 5, 6])
  print(m1 * m2)
  print(m2 * m1)

if __name__ == '__main__':
  main()
