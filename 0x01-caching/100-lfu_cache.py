#!/usr/bin/python3
""" LFUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ A LFU caching system
    """
    MAX_ITEMS = BaseCaching.MAX_ITEMS
    times_used = {}

    def __init__(self):
        """ Class constructor
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(list(self.cache_data.keys())) + 1 > self.MAX_ITEMS:
                least_used = min([val for _, val in self.times_used.items()])
                for key2, value in self.times_used.items():
                    if value == least_used:
                        del self.cache_data[key2]
                        del self.times_used[key2]
                        print(f'DISCARD: {key2}')
                        break

            self.cache_data[key] = item
            if key in list(self.times_used.keys()):
                self.times_used[key] += 1
            else:
                self.times_used[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key in list(self.cache_data.keys()):
            self.times_used[key] += 1
            return self.cache_data.get(key)
