#!/usr/bin/env python3
"""
A module that concatenates two strings
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings
    """
    str3 = "{}{}".format(str1, str2)
    return str3
