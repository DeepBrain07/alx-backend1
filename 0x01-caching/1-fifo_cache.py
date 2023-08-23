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
            if len(list(self.cache_data.keys())) + 1 > self.MAX_ITEMS \
                    and key not in list(self.cache_data.keys()):
                key2 = list(self.cache_data.keys())[0]
                del (self.cache_data[key2])
                print(f'DISCARD: {key2}')
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key:
            return self.cache_data.get(key)
