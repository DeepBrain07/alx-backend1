#!/usr/bin/python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFO caching system
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
            if len(list(self.cache_data.keys())) >= self.MAX_ITEMS\
                    and key not in list(self.cache_data.keys()):
                lastkey, _ = self.cache_data.popitem()
                print(f'DISCARD: {lastkey}')
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
