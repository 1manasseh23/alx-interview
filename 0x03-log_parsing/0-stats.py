#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
"""
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
counter = 0

try:
    for i in sys.stdin:
        counter += 1
        data = i.split()
        try:
            status = data[-2]
            total_size += int(data[-1])
            if status in status_codes:
                status_codes[status] += 1
        except BaseException:
            pass
        if counter == 10:
            print("File size: {:d}".format(total_size))
            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print("{}: {:d}".format(k, v))
            counter = 0
except KeyboardInterrupt:
    pass
finally:
    print("File size: {:d}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {:d}".format(k, v))
