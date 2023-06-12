#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_character = sentence[0] if length > 0 else "None"
    tupl = length, first_character
    return(tupl)
