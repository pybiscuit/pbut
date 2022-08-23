import sys
import os
import argparse
import re

parser = argparse.ArgumentParser(description='python implmented cut. cut OPTION FILE. if no file is given use stdin')
parser.add_argument('-b', '--bytes',  action='store', help='select byte range to cut and return. byte range starts at 1.')
parser.add_argument('-c', '--character', action='store', help='select character range to cut and return. character range starts at 1.')
parser.add_argument('files', action='store', type=str, help='list of files to cut from.', nargs='?')
args = parser.parse_args()

print(args)

if not args.files:
    pin = input('>>> ')
    if args.character:
        idx = args.character.split('-')
        print(pin[int(idx[0]):int(idx[1])+1])
    if args.bytes:
        idx = args.bytes.split('-')
        pt_bytes = bytes(pin, 'utf-8')
        print(pt_bytes[int(idx[0]):int(idx[1])+1])
else:
    for file in args.files:

