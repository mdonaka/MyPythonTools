#!/usr/bin/env python3
""" Design Pattern"""

__author__ = "mdonaka"
__date__ = "2020/03/25"


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
