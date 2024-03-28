#!/usr/bin/env python3


""" module using PyMongo """


def update_topics(mongo_collection, name, topics):
    """
    Inserts new document in collection
    Args: mongo_collection, name, topics
    Return: nothing
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
