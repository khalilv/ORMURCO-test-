import datetime


class Cache:

    def __init__(self):
        self.cache = {}
        self.maximumSize = 10
        self.currentSize = 0

    def isEmpty(self):
        return self.cache == {}

    def __contains__(self, item):
        return item in self.cache

    def __sizeof__(self):
        return self.currentSize

    def view(self):
        return self.cache

    def update(self, key, value):
        if self.currentSize >= self.maximumSize and key not in self.cache:
            self.delete()

        self.cache[key] = {'time': datetime.datetime.now().isoformat(), 'value':value}
        self.currentSize += 1

    def delete(self):
        # get key of least recently used element in cache
        lru_entry = None
        for i in self.cache:
            if lru_entry is None:
                lru_entry = i
            elif self.cache[i]['time'] < self.cache[lru_entry]['time']:
                lru_entry = i
        self.cache.pop(lru_entry)
        self.currentSize -= 1

