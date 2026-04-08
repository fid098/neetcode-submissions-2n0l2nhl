class TimeMap:
    """
    we store multiple values for the same key at specific time
    retrieve the key's value at a specific time 
    in set: we store the key with the value at the given time
    in get: return the most recent value of key if set was previously called on it
    and the most recent timestamp for that key
    prev_timestamp <= timestamp
    if no values return ""
    """
    def __init__(self):
        self.timemap = {}  #initialise the hashmap

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {}
        if timestamp not in self.timemap[key]:
            self.timemap[key][timestamp] = []
        self.timemap[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:  #if the key is not in there return ""
            return ""

        timestamps = sorted(self.timemap[key].keys()) # we sort all the timestamps

        l, r = 0, len(timestamps) - 1
        result = ""

        while l <= r: 
            mid = l + ((r - l) // 2)
            if timestamps[mid] <= timestamp:  #if the mid is <= timestamp store 
                result = timestamps[mid]
                l = mid + 1 #move l inside to find bigger
            else:
                r = mid - 1  #if > move r inside to find smaller 

        return "" if result == "" else self.timemap[key][result][-1]
        #return the value 



    

        
