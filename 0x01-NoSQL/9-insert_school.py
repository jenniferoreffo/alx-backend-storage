#!/usr/bin/env python3


""" module using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document in collection
    Args: mongo_collection, **key word arguments
    Return: obj.inserted_id
    """
    obj = mongo_collection.insert_one(kwargs)

    return obj.inserted_id
