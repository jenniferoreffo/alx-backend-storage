#!/usr/bin/env python3


""" module using PyMongo """


def top_student(mongo_collection):
    """
    Returns all students sorted by avg.
    Args: mongo_collection, name, topics
    Return: mongo_collection.aggregrate
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
