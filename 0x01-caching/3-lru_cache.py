#!/usr/bin/python3
"""
LRUCache module that inherits from BaseCaching

Author: Gadoskey
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that implements a caching system
    following the LRU (Least Recently Used) algorithm.

    Methods:
        put(key, item): Adds an item to the cache with LRU eviction.
        get(key): Retrieves an item by key from the cache.
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of insertion order for LRU

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm.

        Parameters:
            key (str): The key under which to store the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        # If the key is already in the cache, we update the item
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            # If cache is full, remove the least recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the oldest item in cache
                least_used = self.order.pop(0)
                del self.cache_data[least_used]
                print(f"DISCARD: {least_used}")

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
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
