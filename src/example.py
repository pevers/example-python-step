import sys
import pyfiglet

if __name__ == "__main__":
  print(pyfiglet.figlet_format(sys.argv[1]), end="")
