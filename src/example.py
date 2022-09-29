import sys
import pyfiglet

if __name__ == "__main__":
  with open(sys.argv[0], "r") as f:
    print(pyfiglet.figlet_format(f.read()), end="")
