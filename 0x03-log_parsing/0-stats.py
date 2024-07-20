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

def process_line(line, total_size, status_counts):
    """Processes a valid log line and updates metrics."""
    match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)', line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        total_size += file_size
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status_code] += 1
    return total_size, status_counts

def print_stats(total_size, status_counts):
    """Prints the calculated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    """Main function that reads lines and prints statistics."""
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                total_size, status_counts = process_line(line, total_size, status_counts)
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
                    print()  # Add a newline for separation

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
