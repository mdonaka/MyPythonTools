#!/usr/bin/env python3
""" Design Pattern"""

__author__ = "mdonaka"
__date__ = "2020/03/25"

from collections.abc import Iterator
from typing import Callable, Type


class Singleton(object):
    def __new__(cls: Type["Singleton"]) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance: "Singleton" = super(Singleton, cls).__new__(cls)
            return cls._instance
        setattr(cls, "__init__", lambda self: None)
        return cls._instance


class i(Iterator):
    """
    reference:
    https://dawn.hateblo.jp/entry/2019/02/27/131547
    https://gist.github.com/edvakf/90312
    """

    def __init__(self, obj) -> None:
        self.__iter = iter(obj)

    def to_list(self) -> list:
        lst = list(self.__iter)
        self.__iter = iter(lst)
        return lst

    def map(self, func: Callable) -> "i":
        return i(map(func, self.__iter))

    def filter(self, func: Callable) -> "i":
        return i(filter(func, self.__iter))

    def sort(self, *args, **kw) -> "i":
        return i(sorted(list(self.__iter), *args, **kw))

    def reverse(self) -> "i":
        return i(reversed(list(self.__iter)))

    def __iter__(self):
        return self.__iter.__iter__()

    def __next__(self):
        return self.__iter.__next__()
