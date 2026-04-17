class Solution:
    def groupAnagrams(self, strs):
        pairs = []
        for s in strs:
            key = "".join(sorted(s))
            pairs.append((key, s))
        pairs.sort()

        result = []
        current_group = [pairs[0][1]]
        for i in range(1, len(pairs)):
            if pairs[i][0] == pairs[i - 1][0]:
                current_group.append(pairs[i][1])
            else:
                result.append(current_group)
                current_group = [pairs[i][1]]

        result.append(current_group)

        return result