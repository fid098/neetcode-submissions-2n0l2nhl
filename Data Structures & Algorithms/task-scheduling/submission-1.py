class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        maxheap = most frequent task 
        when we pop from the maxheap(execute a task), increment the timer
        we want to decrement it since we have execute one of that task
        the new count is added to the queue with the idletime 
        when the time of the top of the queue is reached, the count is added the maxheap
        and popped from the queue
        """

        count = Counter(tasks) #dic(task: count)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #this should hold (count, idletime)

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                