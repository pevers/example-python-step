import sys
import pyfiglet

if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    print(pyfiglet.figlet_format(), end="")
