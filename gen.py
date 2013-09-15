#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Usage example:

$ python gen.py ru.txt result.txt 10

"""

import argparse
import random


parser = argparse.ArgumentParser(description='String generator.')
parser.add_argument('alphabet', type=str,
                    help='path to the alphabet file')
parser.add_argument('output', type=str,
                    help='output path')
parser.add_argument('size', type=int,
                    help='output size in GB')
parser.add_argument('--output-buffer', type=int, default=10 << 10,
                    help='output buffer size in KB [DEFAULT: 10MB]')
parser.add_argument('--min-spaces', type=int, default=0,
                    help='minimum number of spaces per string [DEFAULT: 0]')
parser.add_argument('--max-spaces', type=int, default=3,
                    help='maximum number of spaces per string [DEFAULT: 3]')
parser.add_argument('--min-string-length',
                    type=int, default=20,
                    help='minimum word length [DEFAULT: 20]')
parser.add_argument('--max-string-length',
                    type=int, default=30,
                    help='maximum word length [DEFAULT: 30]')


def load_alphabet(path):
    with open(path, 'r') as fd:
        alphabet = fd.read().decode('utf-8')
    return alphabet

def main():
    args = parser.parse_args()
    alphabet = load_alphabet(args.alphabet)
    max_size = args.size << 30
    min_spaces = args.min_spaces
    max_spaces = args.max_spaces
    min_string_length = args.min_string_length
    max_string_length = args.max_string_length

    with open(args.output, 'wb', args.output_buffer << 10) as fd:
        size = 0
        run = True
        while run:
            string = u''
            letters_count = random.randint(min_string_length,
                                           max_string_length)
            spaces_count = random.randint(min_spaces,
                                          max_spaces)
            spaces = [random.randint(1, letters_count-1)
                      for _ in range(spaces_count)]
            for i in range(letters_count):
                string += random.choice(alphabet) if i not in spaces else ' '
            string += '\n'
            encoded_string = string.encode('utf-8')
            size += len(encoded_string)
            if size > (max_size):
                run = False
                encoded_string = string[:(max_size - size)].encode('utf-8')
            if size == (max_size):
                run = False
            fd.write(encoded_string)


if __name__ == "__main__":
    main()
