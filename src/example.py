import sys
import pyfiglet
from os.path import exists

if __name__ == "__main__":
  print(f"Input {sys.argv[[1]]}")
  print(f"Exists? {exists(sys.argv[1])}")
  with open(sys.argv[1], "r") as f:
    print(pyfiglet.figlet_format(), end="")
