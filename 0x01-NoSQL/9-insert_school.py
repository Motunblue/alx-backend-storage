#!/usr/bin/env python3
"""Insert School Module"""


def insert_school(mongo_collection, **kwargs):
    """Insert school in a collection"""
    school = mongo_collection.insert_one(kwargs)
    return school.inserted_id
