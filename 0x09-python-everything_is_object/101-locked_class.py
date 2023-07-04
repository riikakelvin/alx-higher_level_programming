#!/usr/bin/python3
class LockedClass:
    '''user can't initiate new attribute(lockedclass)
    rather than attributes named "first_name" '''
    __slots__ = ["first_name"]
