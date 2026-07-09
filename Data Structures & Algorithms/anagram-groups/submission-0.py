class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        def hash(s):
            key = [0] * 26
            for char in s:
                index = ord('a') - ord(char)
                key[index] += 1
            return tuple(key)

        for s in strs:
            key = hash(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return list(groups.values())
   