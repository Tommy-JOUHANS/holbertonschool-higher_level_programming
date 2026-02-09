#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:
    - Total file size up to that point.
    - Count of lines by status code up to that point.
"""

import sys


class Magic:
    """Class that defines a Magic object with a dic and size."""
    def __init__(self):
        """Initialize a Magic object with a dic and size."""
        self.dic = {}
        self.size = 0

    def init_dic(self):
        """Initialize the dic with status codes."""
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_status_code(self, status):
        """Add a status code to the dic."""
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        """Print the info."""
        print("File size: {}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] > 0:
                print("{}: {}".format(key, self.dic[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dic()
    nlines = 0

    try:
        for line in sys.stdin:
            nlines += 1
            if nlines == 10:
                magic.print_info()
                nlines = 0
            parts = line.split()
            if len(parts) < 9:
                continue
            try:
                magic.size += int(parts[-1])
            except ValueError:
                pass
            magic.add_status_code(parts[-2])
    except KeyboardInterrupt:
        pass
    finally:
        magic.print_info()
