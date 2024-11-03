#!/usr/bin/python3
"""
LIFOCache module that inherits from BaseCaching

Author: Gadoskey
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a caching system
    following the LIFO (Last In First Out) algorithm.

    Methods:
        put(key, item): Adds an item to the cache with LIFO eviction.
        get(key): Retrieves an item by key from the cache.
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of insertion order for FIFO

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.

        Parameters:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        # If the key is already in the cache, we update the item
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            # If cache is full, remove the oldest item based on LIFO
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the oldest item in cache
                latest_key = self.order.pop(len(self.cache_data) - 1)
                del self.cache_data[latest_key]
                print(f"DISCARD: {latest_key}")

            # Insert the new key-value pair into the cache
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item by key from the cache.

        Parameters:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if found, otherwise None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
