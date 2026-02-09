#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics:
- Total file size up to that point.
- Count of lines by status code up to that point.
"""

import sys


class Magic:
    """Class that defines a Magic object with a dict and size."""
    def __init__(self):
        self.size = 0
        self.dic = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }

    def add_status_code(self, status):
        """Increment count of a status code."""
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self):
        """Print current statistics."""
        print("File size: {}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] > 0:
                print("{}: {}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    nlines = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            try:
                magic.size += int(parts[-1])
                # status code
                magic.add_status_code(parts[-2])

            except (IndexError, ValueError):
                pass

            nlines += 1
            if nlines == 10:
                magic.print_info()
                nlines = 0

    except KeyboardInterrupt:
        pass
    finally:
        magic.print_info()
