
from libs.matrix import Matrix

def main():
  m = Matrix(3,4,[1,2,3,4,5,6,7,8,9,10,11,12])
  m2 = Matrix(3,4,[5,5,5,5,5,5,5,5,5,5,5,5])
  m3 = m + m2
  print(m3.get_row(3))

if __name__ == '__main__':
  main()

