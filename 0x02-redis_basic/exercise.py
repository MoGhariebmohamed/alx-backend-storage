#!/usr/bin/env python3
"""
for reddis excersis
"""

import sys
from uuid import uuid4
from typing import Union, Optional, Callable
import redis
from functools import wraps

all_types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    the metod to call class
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        to wrap the class
        """
        self.redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    for the redis cash db
    """

    def __init__(self):
        """
        initiate redis module
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: all_types) -> str:
        """
        get random key generated uuid stored in redis db
        data: all data types
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> all_types:
        """
        convert data types to required format
        key: the key value
        fn: optional callabe argument
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self: bytes) -> str:
        """
        get the string
        """
        return self.decode("utf-8")

    def get_int(self: bytes) -> int:
        """
        get the integer
        """
        return int.from_bytes(self, sys.byteorder)
