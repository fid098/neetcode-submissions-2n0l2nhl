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

        seen = 0  #the most recent time would be the max time

        for time in self.timemap[key]:  #iterate through the keys
            if time <= timestamp:   #any values that are <= timestamp
                seen = max(seen, time)  #find which one is more recent 
        return "" if seen == 0 else self.timemap[key][seen][-1]  
        #return the emotion at that timestamp 
    

        
