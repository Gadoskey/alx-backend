#!/usr/bin/python3
"""
BasicCache module that inherits from BaseCaching

Author: Yusuf Mustapha Opeyemi
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class with put and get methods to store and retrieve items
    in a simple cache.

    Methods:
        put(key, item): Adds an item in the cache.
        get(key): Retrieves an item from the cache.
    """

    def put(self, key, item):
        """
        Add an item in the cache.

        Parameters:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        # Store the item in the cache with the given key
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Parameters:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if found, otherwise None.
        """
        if key is None:
            return None
        # Return the item associated with the key, or None if it doesn't exist
        return self.cache_data.get(key)
