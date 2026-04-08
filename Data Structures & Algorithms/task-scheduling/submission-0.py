class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)     #gets the counts for each as a dictionary(letter: count)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        #the heap has the task with the highest count at the top 


        time = 0  #time to complete all tasks 
        q = deque()  # pairs of [-cnt, idleTime] (Task: count, idletime)

        while maxHeap or q:
            time += 1  
            #if there is still a task in the heap or queue
            if not maxHeap:
                #if no more tasks
                time = q[0][1] #gets the idletime of the top of the queue
            else:
                #if there are tasks left, pop the max
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 


