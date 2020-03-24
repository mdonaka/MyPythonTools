#!/usr/bin/env python3
""" Design Pattern"""

__author__ = "mdonaka"
__date__ = "2020/03/25"


class Singleton(object):
    @classmethod
    def get_instance(cls, input):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance
