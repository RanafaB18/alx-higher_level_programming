#!/usr/bin/python3
"""Defines function 'print_stats' """


def print_stats(status_codes, size):
    """Log stats"""
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys


    size = 0
    status_codes = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split(" ")
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                stat_code = line[-2]
                if stat_code in codes:
                    if status_codes.get(stat_code, -1) == -1:
                        status_codes[stat_code] = 1
                    else:
                        status_codes[stat_code] += 1
            except IndexError:
                pass
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
