
"""
This module defines an LRUCache.

Constraints:
1. May only hold upto ten items at a time.
2. Must be able to synchronise multiple requests.
3. Must be able to update its cache.
多线程安全缓存，缓存最近访问的记录
"""

import threading
from collections import OrderedDict


class LRUCache(object):

    def __init__(self, size=10):

        # this variables maps image names to file locations
        self.cache = OrderedDict()
        self.size = size
        self.lock = threading.Lock()

    def insert(self, key, value):

        """
        Insert a new image into our cache. If inserting would exceed our cache size,
        then we shall make room for it by removing the least recently used.
        """

        with self.lock:
            self.limit_length()
        self.cache[key] = value
        self.size -= 1

    def get(self, key):

        """
        Retrieve an image from our cache, keeping note of the time we last
        retrieved it.
        """

        with self.lock:
            if key in self.cache:
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
            else:
                """
                向其他服务器请，获取value值
                self.cache_length()
                self.cache[key] = value
                """
                raise KeyError("Not found!")

    def limit_length(self):
        while self.size > 0:
            self.cache.popitem(last=False)
            self.size += 1