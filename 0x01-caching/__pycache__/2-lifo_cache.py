#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFO caching system
    """
    MAX_ITEMS = BaseCaching.MAX_ITEMS

    def __init__(self):
        """ Class constructor
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
            key = list(self.cache_data.keys())[0]
            del (self.cache_data[key])
            print(f'DISCARD: {key}')

    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
