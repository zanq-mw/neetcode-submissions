class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        options = sorted(list(self.store[key].keys()))
        l = 0
        r = len(options) -1
        if timestamp < options[l]:
            return ""
        if timestamp > options[r]:
            return self.store[key][options[r]]
        key1 = 0
        while l <= r:
            m = (l+r) //2
            if options[m] > timestamp:
                r = m-1
            else:
                if options[m] > key1:
                    key1 = options[m]
                l = m+1
        # if key1 > timestamp:
        #     return ""
        return self.store[key][key1]


