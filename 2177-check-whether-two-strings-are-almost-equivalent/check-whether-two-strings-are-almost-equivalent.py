class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w=word1+word2
        w=set(w)
        for i in w:
            if abs(word1.count(i)-word2.count(i))>3:
                return False
        return True

        