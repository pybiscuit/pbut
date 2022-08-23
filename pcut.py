import sys
import os
import argparse
import re

parser = argparse.ArgumentParser(description='python implmented cut. cut OPTION FILE. if no file is given use stdin')
parser.add_argument('-b', '--bytes',  action='store', help='select byte range to cut and return. byte range starts at 1.')
parser.add_argument('-c', '--character', action='store', help='select character range to cut and return. character range starts at 1.')
parser.add_argument('files', action='store', type=str, help='list of files to cut from.', nargs='+')
args = parser.parse_args()

print(args)

def split_ids(arg=None):
    if arg == 'char':
        return [int(i) for i in args.character.split('-')]
    else:
        return [int(i) for i in args.bytes.split('-')]

def std_parse():
    pin = input('>>> ')
    if args.character:
        idx = split_ids('char')
        print(pin[idx[0]:idx[1]+1])
    if args.bytes:
        idx = split_ids()
        pt_bytes = bytes(pin, 'utf-8')
        print(pt_bytes[idx[0]:idx[1]+1])

def file_parse():
    if args.character:
        idx = split_ids('char')
        for file in args.files:
            with open(file, 'r') as f:
                for line in f.readlines():
                    print(line[idx[0]:idx[1]+1]) 
        
if not args.files:
    std_parse()
else:
    file_parse()
