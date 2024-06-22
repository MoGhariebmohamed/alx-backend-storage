#!/usr/bin/env python3
"""
for insert docs in python
"""


def schools_by_topic(mongo_collection, topic):
    """
    changes all topics of a school document
    """
     return mongo_collection.find({"topics": topic})
