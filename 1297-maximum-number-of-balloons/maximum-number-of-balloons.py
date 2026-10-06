class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mini = len(text)
        for c in ['b', 'a', 'l', 'o', 'n']:
            if c in ['l', 'o']:
                mini = min(text.count(c) // 2, mini)
            else:
                mini = min(text.count(c), mini)
        return mini