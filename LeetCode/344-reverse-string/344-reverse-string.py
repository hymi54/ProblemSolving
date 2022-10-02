class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, len(s)//2):
            s[i], s[-1 - i] = s[-1 - i], s[i]
        