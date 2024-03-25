#!/usr/bin/env python3


""" a Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """
    function list_all
    Args: mongo_collection
    Return: Return an empty list if no document in the collection
    """
    documents = list(mongo_collection.find({}))

    # Return an empty list if no documents found
    if not documents:
        return []

    return documents
