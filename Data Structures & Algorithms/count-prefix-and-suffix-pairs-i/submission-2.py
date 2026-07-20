class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a , b):
            n = len(a)
            m = len(b)

            if n > m:
                return False
            str1 = b[:n]
            str2 = b[m -n:]
            return str1 == a and str2 == a
        count = 0
        for i in range(len(words)):
            for j in range(i + 1 , len(words)):
                if isPrefixAndSuffix(words[i] , words[j]):
                    count+= 1
        return count
