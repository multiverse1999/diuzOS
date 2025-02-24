import re
import sys

def printf(format_string, *args):
    print(format_string % args, end='')

def scanf(format_string):
    input_data = input()
    pattern = format_string.replace('%d', r'(-?\d+)').replace('%f', r'(-?\d+\.\d+)').replace('%s', r'(\S+)')
    match = re.match(pattern, input_data)
    if match:
        return match.groups()
    return None

