class ListNode:
    #this initialises the node 
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.dummyleft = ListNode(0, 0) #initialise head and tail with key and value 0, 0
        self.dummyright = ListNode(0, 0)
        self.dummyleft.next = self.dummyright
        self.dummyright.prev = self.dummyleft

    def add(self, node):
        #adds the node to the start 
        nxt = self.dummyleft.next 
        self.dummyleft.next = node
        node.prev = self.dummyleft
        node.next = nxt
        nxt.prev = node

    def delete(self, node):
        #removes the node and connects either side 
        tmp1 = node.next 
        tmp2 = node.prev 
        tmp2.next = tmp1
        tmp1.prev = tmp2

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.delete(self.hashmap[key]) #delete from the end
            self.add(self.hashmap[key]) #add to the start 
            return self.hashmap[key].value #return the value at the node(key points to)
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:  #if key exist
            self.hashmap[key].value = value  #replace the value
            self.delete(self.hashmap[key])  #delete the node from the end 
            self.add(self.hashmap[key])     #add the the start 
        else:
            node = ListNode(key, value)  #if not in hashmap, create a node
            self.add(node)  #add the node to the start 
            self.hashmap[key] = node   #add the key:node to the hashmap
            if len(self.hashmap) > self.capacity:  #if at max capacity 
                tmp1 = self.dummyright.prev  #store the node before the end 
                self.delete(tmp1)  #delete that node 
                del self.hashmap[tmp1.key]  #delete the key:node from the hashmap 
        
