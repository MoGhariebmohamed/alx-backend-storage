#!/usr/bin/env python3
"""
for insert docs in python
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document
    """
     return mongo_collection.find({"topics": topic})
