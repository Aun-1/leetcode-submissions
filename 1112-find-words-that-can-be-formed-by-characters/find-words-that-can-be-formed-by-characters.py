class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        ans = 0
        for w in words:
            found = True
            for c in set(w):
                if w.count(c) > chars.count(c):
                    found = False
            if found:
                ans += len(w)
        return ans