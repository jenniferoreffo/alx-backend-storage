#!/usr/bin/env python3


""" Redis Db module """


import redis
import sys
from functools import wraps
from typing import Union, Callable, Optional
from uuid import uuid4


UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    a system to count the times methods of the Cache class are called
    Args:
    Return:
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrap
        Args: self, *args, **kwargs
        Return
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    add its input parameters to one list
    Args:
    Return:
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapp """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


class Cache:
    """ Cache redis class """

    def __init__(self):
        """
        constructor of the redis model
        Args: self
        Return: key
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        Generate a random key
        Args: self
        Return: key
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """
        Convert Data back to the desired format
        Args: self, key
        Return data
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> str:
        """ string utf-8 """
        return self.decode("utf-8")

    def get_int(self: bytes) -> int:
        """ number """
        return int.from_bytes(self, sys.byteorder)
