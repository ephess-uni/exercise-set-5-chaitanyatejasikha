""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program applies a standard scale transform to the data in infile and writes it to outfile.')
    parser.add_argument('infile',help='provide input file path',nargs='?')
    parser.add_argument('outfile',help='provide output file path',nargs='?')
    args = parser.parse_args()
    normed = (raw_data - raw_data.mean(axis=0)) / raw_data.std(axis=0)
    processed = normed
    np.savetxt(args.outfile, processed, fmt='%.2e')

