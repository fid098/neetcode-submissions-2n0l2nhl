class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        while q:
            word, steps = q.popleft()
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for neighbour in patterns[pattern]:
                    if neighbour == endWord:
                        return steps + 1
                    if neighbour not in seen:
                        seen.add(neighbour)
                        q.append([neighbour, steps + 1])
        
        return 0