#!/usr/bin/python3
def roman_to_int(roman_string):
       if roman_string is None or type(roman_string) != str:
        return 0
    sample_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [sample_data[x] for x in roman_string] + [0]
    conversion = 0

    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            conversion += num[i]
        else:
            conversion -= num[i]

    return conversion

