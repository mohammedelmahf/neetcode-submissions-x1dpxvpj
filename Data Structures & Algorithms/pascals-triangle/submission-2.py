class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tringle = []

        for i in range(numRows):
            if i == 0:
                tringle.append([1])
                continue
            prev = tringle[i - 1]
            new = [1]
            for j in range(1 , len(prev)):
                new.append(prev[j - 1] + prev[j])
            new.append(1)
            tringle.append(new)
        return tringle

