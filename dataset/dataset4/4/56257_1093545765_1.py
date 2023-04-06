import zipfile
import os

def main():
  szTestDir = os.path.dirname(__file__)
  szFile = os.path.join(szTestDir, 'test.zip')
  z = zipfile.ZipFile(szFile)
  print(z.namelist()[0])
  z.extract(z.namelist()[0])

if __name__ == '__main__':
  main()