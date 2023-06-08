#!/usr/bin/python3
if __name__=="__main__":
    import sys

    arg = sys.argv
    num_count = len(arg) - 1

    if num_count == 0:
        print("{:d}".format(num_count))
    
    else:
        n = 1
        added = 0
        while n <= num_count:
            added = added + int(argv[n])
            n += 1
        print("{:d}".format(added))
