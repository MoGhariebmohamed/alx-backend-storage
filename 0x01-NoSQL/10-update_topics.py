#!/usr/bin/env python3
"""
for insert docs in python
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document
    """
    mongo_collection.update_many({name: name, {"$set": {"topice": topics}})
