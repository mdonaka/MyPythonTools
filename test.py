#!/usr/bin/env python3
"""stop watch """

__author__ = "mdonaka"
__date__ = "2020/03/05"
import time
from functools import wraps
from logging import DEBUG, basicConfig, getLogger

from MyPythonTools.Timer import stop_watch

logger = getLogger(__name__)


@stop_watch
def f(n: int):
    for _ in range(n):
        a = 10 * 5
        a = a


if __name__ == "__main__":
    basicConfig(level=DEBUG)

    for i in [pow(2, t) for t in range(10, 20)]:
        f(i)
