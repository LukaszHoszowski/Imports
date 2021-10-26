import bz2

from .. import utils

opener = bz2.open

if __name__ == '__main__':
    utils.writer.main(opener)

# python demo_reader/compressed/gzipped.py elo.gz ala ma kota
# python demo_reader/compressed/bzipped.py elo.bz2 ala ma kota