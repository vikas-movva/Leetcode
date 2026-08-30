#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            anagrams[sorted_str].append(str)
        
        return list(anagrams.values())
# @lc code=end

"""Original version
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = []
        for str in strs:
            map = {}
            for char in str:
                map[char] = map.get(char, 0) + 1
            maps.append(map)
        anagrams = []
        indexes = list(range(len(strs)))
        while len(indexes) > 0:
            index = indexes[0]
            anagram = [strs[index]]
            for i in indexes[1:]:
                if maps[index] == maps[i]:
                    anagram.append(strs[i])
                    indexes.remove(i)
            anagrams.append(anagram)
            indexes.pop(0)
        return anagrams
"""


