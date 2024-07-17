#!/usr/bin/python3
"""This  a script that reads stdin line by line
and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260
    HTTP/1.1" <status code> <file size> (if the format is not
    this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see
input format above) Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404,
    405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
    format: <status code>: <number>
status codes should be printed in ascending oder"""
import sys
import re
from collections import defaultdict


def main():
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    # Define the regex pattern for the input format
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line)

            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))

                # Update total size and status counts
                total_size += file_size
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_count[status_code] += 1

            # After every 10 lines, print the metrics
            if line_count % 10 == 0:
                print_metrics(total_size, status_count)

    except KeyboardInterrupt:
        # Print metrics on keyboard interrupt
        print_metrics(total_size, status_count)
        sys.exit(0)


def print_metrics(total_size, status_count):
    print(f"File size: {total_size}")
    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")


if __name__ == "__main__":
    main()
