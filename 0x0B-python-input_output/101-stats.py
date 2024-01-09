#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
"""


import sys

total_size = 0
s_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            elements = line.split()
            size = int(elements[-1])
            status_code = int(elements[-2])

            total_size += size
            s_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(s_codes.keys()):
                    if s_codes[code] != 0:
                        print("{}: {}".format(code, s_codes[code]))

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(s_codes.keys()):
        if s_codes[code] != 0:
            print("{}: {}".format(code, s_codes[code]))
    sys.exit(0)
