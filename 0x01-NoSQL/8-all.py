#!/usr/bin/env python3
"""List all Module"""


def list_all(mongo_collection):
    """List all doucment in collection"""
    return [x for x in mongo_collection.find()]
