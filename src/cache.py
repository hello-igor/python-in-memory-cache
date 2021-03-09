import re
import time
import threading


class MyCache():

    def __init__(self):
        self._cache = {}
        self._cache_time = {}
        x = threading.Thread(target=self._watch, args=(), daemon=True)
        x.start()

    def _watch(self):
            try:
                current_time = time.time()
                for i in self._cache.keys():
                    if current_time > self._cache_time[i][0] + self._cache_time[i][1]:
                        self._cache.pop(i)
                        self._cache_time.pop(i)
            except: 'Cache changed!'
            time.sleep(0.8)
            self._watch()

    def set_item(self, key, value, ttl=None):  
        self._cache[key] = value
        if ttl is not None:
            creation_time = time.time()
            self._cache_time[key] = [creation_time, ttl]

    def get_item(self, key):
        if key in self._cache.keys():
            return self._cache[key]
            print(self._cache[key])
        else:
            return 'No such key!'

    def del_item(self, key):
        if key in self._cache.keys():
            self._cache.pop(key)
            if key in self._cache_time.keys():
                self._cache_time.pop(key)
            return 'Deleted!'
        else:
            return 'No such key!'

    def keys(self, pattern):
        result = []
        try:
            for i in self._cache.keys():
                if re.findall(pattern, str(i)) != []:
                    result.append(i)
        except: 'Cache changed!'
        if result == []:
            return "No such keys!"
        else:
            return result