import sys

from oblique.oblique import Oblique


if __name__ == '__main__':
    try:
        o = Oblique()
        o.open_doc(sys.argv[1])
    except:
        print('Usage:\n\toblique filename.html')
