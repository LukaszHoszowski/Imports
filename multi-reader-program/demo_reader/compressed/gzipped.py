import gzip

from ..utils import writer

opener = gzip.open

if __name__ == '__main__':
    writer.main(opener)

# python demo_reader/compressed/gzipped.py elo.gz ala ma kota
