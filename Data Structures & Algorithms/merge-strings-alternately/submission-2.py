class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        length = 0
        for i in range(min(len(word1), len(word2))):
            word = word + word1[i] + word2[i]
            length = i

        if len(word1) > len(word2):
            for x in range(length + 1, len(word1)):
                word = word + word1[x]
        

        if len(word2) > len(word1):
            for x in range(length + 1, len(word2)):
                word = word + word2[x]

        return word
