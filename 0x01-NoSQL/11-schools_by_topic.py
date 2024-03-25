
#!/usr/bin/env python3


""" module using PyMongo """


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args: mongo_collection, topic
    Return: mongo_collection "topic"
    """
    return mongo_collection.find({"topics": topic})

