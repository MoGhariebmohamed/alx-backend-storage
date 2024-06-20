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

    def store(self, data: all_types) -> str:
       """
       get random key generated uuid stored in redis db
       data: all data types
       """

       key = str(uuid4())
       self._redis.mset({key: data})
       return key

