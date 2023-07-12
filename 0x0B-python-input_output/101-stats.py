#!/usr/bin/python3

"""Defines a script that reads stdin line by line and computes metrics."""


from collections import defaultdict

VALID_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}
STATS_PRINT_INTERVAL = 10


def extract_info(line):
    """Extracts information from a line"""
    parts = line.split()
    try:
        size = int(parts[-1])
        code = parts[-2]
        return size, code
    except (IndexError, ValueError):
        return 0, None


def print_stats(size, status_codes):
    """Prints accumulated metrics."""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            cur_size, cur_code = extract_info(line)

            size += cur_size

            if cur_code in VALID_CODES:
                status_codes[cur_code] += 1

            if line_count % STATS_PRINT_INTERVAL == 0:
                print_stats(size, status_codes)

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
