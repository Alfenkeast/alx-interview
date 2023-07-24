#!/usr/bin/python3
""" doc """
import sys


if __name__ == "__main__":
    i = 0
    status = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    fileSize = 0

    def printstats(fileSize, status):
        """ doc """
        print("File size: {:d}".format(fileSize))
        for key in sorted(status.keys()):
            if status[key] != 0:
                print("{}: {:d}".format(key, status[key]))

    try:
        for line in sys.stdin:
            words = line.split()
            if len(words) >= 2:
                if words[-2] in status.keys():
                    status[words[-2]] += 1
                fileSize += int(words[-1])
                i += 1
                if not i % 10:
                    printstats(fileSize, status)
        printstats(fileSize, status)
    except KeyboardInterrupt:
        printstats(fileSize, status)
        raise
