class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mini = len(text)
        w = ['b', 'a', 'l', 'l','o','o', 'n']
        for c in w:
            mini = min(text.count(c) // w.count(c), mini)

        return mini