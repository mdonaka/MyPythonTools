#!/usr/bin/env python3
""" Design Pattern"""

__author__ = "mdonaka"
__date__ = "2020/03/25"

from typing import Type


class Singleton(object):
    def __new__(cls: Type["Singleton"]) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance: "Singleton" = super(Singleton, cls).__new__(cls)
            return cls._instance
        setattr(cls, "__init__", lambda self: None)
        return cls._instance
