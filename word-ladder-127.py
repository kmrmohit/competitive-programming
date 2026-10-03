'''
Day 4
3 attempts, 2tle
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList = set(wordList)
        if not endWord in wordList:
            return 0

        from collections import deque
        que = deque()
        que.append((beginWord,1))
        visited = {beginWord: True}
        while que:
            (word,count) = que.popleft()
            if word == endWord:
                return count
            
            for (index, char) in enumerate(word):
                for i in range(0,26):
                    newChar = chr(ord('a') + i)
                    if char != newChar:
                        newWord = word[:index] + newChar + word[index+1:]
                        # print(word, newWord)
                        if not visited.get(newWord) and newWord in wordList:
                            que.append((newWord,count+1))
                            visited[newWord] = True
        
        return 0