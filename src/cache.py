import re
import time
import threading


class MyCache():

    def __init__(self):
        self.cache = {}
        self.cache_time = {}
        self.__watch_thread = threading.Thread(target=self.__watch, args=(), daemon=True)
        self.__watch_thread.start()

    def __watch(self):
            try:
                current_time = time.time()
                for i in self.cache.keys():
                    if current_time > self.cache_time[i][0] + self.cache_time[i][1]:
                        self.cache.pop(i)
                        self.cache_time.pop(i)
            except: 'Cache changed!'
            time.sleep(0.8)
            self.__watch()

    def set_item(self, key, value, ttl=None):  
        self.cache[key] = value
        if ttl is not None:
            creation_time = time.time()
            self.cache_time[key] = [creation_time, ttl]

    def get_item(self, key):
        if key in self.cache.keys():
            return self.cache[key]
            print(self.cache[key])
        else:
            return 'No such key!'

    def del_item(self, key):
        if key in self.cache.keys():
            self.cache.pop(key)
            if key in self.cache_time.keys():
                self.cache_time.pop(key)
            return 'Deleted!'
        else:
            return 'No such key!'

    def keys(self, pattern):
        result = []
        try:
            for i in self.cache.keys():
                if re.findall(pattern, str(i)) != []:
                    result.append(i)
        except: 'Cache changed!'
        if result == []:
            return "No such keys!"
        else:
            return result