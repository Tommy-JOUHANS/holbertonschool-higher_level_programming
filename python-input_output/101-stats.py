#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:
    - Total file size up to that point.
    - Count of lines by status code up to that point.
"""

import sys


def print_stats(total_size, status_codes):
    """Print the accumulated metrics.

    Args:
        total_size (int): Total file size up to that point.
        status_codes (dict): Count of lines by status code up to that point.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                pass

            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

            if sum(status_codes.values()) % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
