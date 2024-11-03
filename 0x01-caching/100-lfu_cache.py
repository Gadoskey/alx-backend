#!/usr/bin/python3
"""
LFUCache module that inherits from BaseCaching

Author: Gadoskey
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        self.frequency = {}  # Tracks frequency of each key
        self.order = []      # Tracks order of keys for LRU within LFU

    def put(self, key, item):
        if key is None or item is None:
            return
        
        # Update existing key
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update frequency and order here
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            # If cache is full, apply eviction policy
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find LFU key or LRU among LFUs
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k in self.order if self.frequency[k] == min_freq]
                
                # Evict the LRU among the LFU keys
                lru_key = lfu_keys[0]
                self.order.remove(lru_key)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print(f"DISCARD: {lru_key}")
            
            # Insert new key-value pair
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Update frequency and order for LRU tracking
        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
