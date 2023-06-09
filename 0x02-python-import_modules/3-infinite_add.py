#!/usr/bin/python3
def add_arg(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d}".format(num))
        return
    else:
        x = 1
        added = 0
        while x <= num:
            added = added + int(argv[x])
            x = x + 1
        print("{:d}".format(added))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)

