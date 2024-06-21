#!/usr/bin/env python3
"""
for list all docs in python
"""


def list_all(mongo_collection):
    """
    the metod to  function that lists all documents in a collection
    """
    return mongo_collection.find()
