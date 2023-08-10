from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph = defaultdict(set)
        all_words = [beginWord] + wordList[:]

        for word in all_words:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                graph[key].add(word)

        def bfs(word):

            q = deque([(word, 1)])
            visited = set()
            while q:
                current_word, count = q.popleft()
                if current_word == endWord:
                    return count
                if current_word in visited:
                    continue
                visited.add(current_word)
                for i in range(len(current_word)):
                    key = current_word[:i] + "*" + current_word[i+1:]

                    for neighbor in graph[key]:
                        if neighbor not in visited:
                            q.append((neighbor, count + 1))
            return 0

        return bfs(beginWord)
