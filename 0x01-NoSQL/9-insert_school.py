#!/usr/bin/env python3
"""
for insert docs in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    that inserts a new document in a collection based on kwargs
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
