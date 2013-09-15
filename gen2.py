#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Usage example:

$ python gen2.py ru.txt result.txt 10

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
parser.add_argument('--min-words-per-string',
                    type=int, default=1,
                    help='minimum words per string [DEFAULT: 1]')
parser.add_argument('--max-words-per-string',
                    type=int, default=4,
                    help='maximum words per string [DEFAULT: 4]')
parser.add_argument('--min-word-length',
                    type=int, default=1,
                    help='minimum word length [DEFAULT: 1]')
parser.add_argument('--max-word-length',
                    type=int, default=20,
                    help='maximum word length [DEFAULT: 20]')


def load_alphabet(path):
    with open(path, 'r') as fd:
        alphabet = fd.read().decode('utf-8')
    return alphabet

def main():
    args = parser.parse_args()
    alphabet = load_alphabet(args.alphabet)
    max_size = args.size << 30
    min_words_per_string = args.min_words_per_string
    max_words_per_string = args.max_words_per_string
    min_word_length = args.min_word_length
    max_word_length = args.max_word_length

    with open(args.output, 'wb', args.output_buffer << 10) as fd:
        size = 0
        run = True
        while run:
            string = []
            words_count = random.randint(min_words_per_string,
                                         max_words_per_string)
            for _ in range(words_count):
                word = u''
                word_length = random.randint(min_word_length,
                                             max_word_length)
                for _ in range(word_length):
                    word += random.choice(alphabet)
                string.append(word)
            string = ' '.join(string)
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
