from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        graph = defaultdict(list)
        words = set(wordList)
        words.add(beginWord)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                graph[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            word, dist = q.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for nxt in graph[pattern]:
                    if nxt == endWord:
                        return dist + 1
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1))
        return 0

