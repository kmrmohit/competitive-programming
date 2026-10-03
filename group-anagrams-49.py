'''
Day 0
1 attempt
'''
class Solution:
    def sort(self, input: str):
        return "".join(sorted(input))
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = dict()
        for (index, input) in enumerate(strs):
            tmp = self.sort(input)
            if groups.get(tmp):
                groups[tmp].append(index)
            else:
                groups[tmp] = [index]
        output = list()
        for items in groups.values():
            output.append([strs[i] for i in items])
        return output