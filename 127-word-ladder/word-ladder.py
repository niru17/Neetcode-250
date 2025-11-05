class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord in wordList and not endWord in wordList:
            return 0
        words=set(wordList)
        q=deque([(beginWord,1)])
        while q:
            word,steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt=word[:i]+c+word[i+1:]
                    if nxt in words:
                        words.remove(nxt)
                        q.append((nxt,steps+1))
        return 0

        