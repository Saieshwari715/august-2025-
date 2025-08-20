class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found=-1
        if needle in haystack:
            for i in range(len(haystack)):
                if(haystack[i:i+len(needle)]==needle):
                    found=i
                    break
        return found
        