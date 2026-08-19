class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasmaping = defaultdict(list)
        for string in strs:
            count = [0]* 26
            for words in string:
                count[ord(words) - ord("a")] += 1
            hasmaping[tuple(count)].append(string)

        return list(hasmaping.values())

        



        