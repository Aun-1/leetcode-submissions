class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
            
        def backtrack(start, current, remaining):      # LINE A
            if remaining == 0:                          # LINE B
                result.append(current[:])               # LINE C
                return                                   # LINE D
            if remaining < 0:                            # LINE E
                return                                    # LINE F

            for i in range(start, len(candidates)):       # LINE G
                current.append(candidates[i])             # LINE H
                backtrack(i, current, remaining - candidates[i])  # LINE I
                current.pop()                              # LINE J
            
        backtrack(0, [], target)
        return result


'''
1.   [A] CALL backtrack(0, [], 7)
2.   [B] remaining==0? No
3.   [E] remaining<0? No
4.   [G,H] i=0: append 2 → [2]
5.   [I] CALL backtrack(0, [2], 5)
6.     [B] remaining==0? No
7.     [E] remaining<0? No
8.     [G,H] i=0: append 2 → [2,2]
9.     [I] CALL backtrack(0, [2,2], 3)
10.      [B] remaining==0? No
11.      [E] remaining<0? No
12.      [G,H] i=0: append 2 → [2,2,2]
13.      [I] CALL backtrack(0, [2,2,2], 1)
14.        [B] remaining==0? No
15.        [E] remaining<0? No
16.        [G,H] i=0: append 2 → [2,2,2,2]
17.        [I] CALL backtrack(0,[2,2,2,2],-1)
18.          [B] No  [E] Yes → [F] return
19.        [J] pop → [2,2,2]
20.        [G,H] i=1: append 3 → [2,2,2,3]
21.        [I] CALL backtrack(1,[2,2,2,3],-2)
22.          [B] No  [E] Yes → [F] return
23.        [J] pop → [2,2,2]
24.        [G,H] i=2: append 6 → [2,2,2,6]
25.        [I] CALL backtrack(2,...,-5) → [E][F] dead
26.        [J] pop → [2,2,2]
27.        [G,H] i=3: append 7 → [2,2,2,7]
28.        [I] CALL backtrack(3,...,-6) → [E][F] dead
29.        [J] pop → [2,2,2]
30.        loop (G) exhausted → function ends, return to step13's call
31.      [J] pop → [2,2]
32.      [G,H] i=1: append 3 → [2,2,3]
33.      [I] CALL backtrack(1, [2,2,3], 0)
34.        [B] remaining==0? YES → [C] SAVE [2,2,3]
35.        [D] return
36.      [J] pop → [2,2]
37.      [G,H] i=2: append 6 → [2,2,6]
38.      [I] CALL backtrack(2,...,-3) → [E][F] dead
39.      [J] pop → [2,2]
40.      [G,H] i=3: append 7 → [2,2,7]
41.      [I] CALL backtrack(3,...,-4) → [E][F] dead
42.      [J] pop → [2,2]
43.      loop (G) exhausted → return to step9's call
44.    [J] pop → [2]
45.    [G,H] i=1: append 3 → [2,3]
46.    [I] CALL backtrack(1, [2,3], 2)
47.      [B] No  [E] No
48.      [G,H] i=1: append 3 → [2,3,3]
49.      [I] CALL backtrack(1,...,-1) → [E][F] dead
50.      [J] pop → [2,3]
51.      [G,H] i=2: append 6 → [2,3,6]
52.      [I] CALL backtrack(2,...,-4) → [E][F] dead
53.      [J] pop → [2,3]
54.      [G,H] i=3: append 7 → [2,3,7]
55.      [I] CALL backtrack(3,...,-5) → [E][F] dead
56.      [J] pop → [2,3]
57.      loop (G) exhausted → return to step5's call
58.    [J] pop → [2]
59.    [G,H] i=2: append 6 → [2,6]
60.    [I] CALL backtrack(2,...,-1) → [E][F] dead
61.    [J] pop → [2]
62.    [G,H] i=3: append 7 → [2,7]
63.    [I] CALL backtrack(3,...,-2) → [E][F] dead
64.    [J] pop → [2]
65.    loop (G) exhausted → return to step1's call
66.  [J] pop → []
67.  [G,H] i=1: append 3 → [3]
68.  [I] CALL backtrack(1, [3], 4)
69.    [B] No  [E] No
70.    [G,H] i=1: append 3 → [3,3]
71.    [I] CALL backtrack(1, [3,3], 1)
72.      [B] No  [E] No
73.      [G,H] i=1: append 3 → [3,3,3]
74.      [I] CALL backtrack(1,...,-2) → [E][F] dead
75.      [J] pop → [3,3]
76.      [G,H] i=2: append 6 → [3,3,6]
77.      [I] CALL backtrack(2,...,-5) → [E][F] dead
78.      [J] pop → [3,3]
79.      [G,H] i=3: append 7 → [3,3,7]
80.      [I] CALL backtrack(3,...,-6) → [E][F] dead
81.      [J] pop → [3,3]
82.      loop (G) exhausted → return to step68's call
83.    [J] pop → [3]
84.    [G,H] i=2: append 6 → [3,6]
85.    [I] CALL backtrack(2,...,-2) → [E][F] dead
86.    [J] pop → [3]
87.    [G,H] i=3: append 7 → [3,7]
88.    [I] CALL backtrack(3,...,-3) → [E][F] dead
89.    [J] pop → [3]
90.    loop (G) exhausted → return to step1's call
91.  [J] pop → []
92.  [G,H] i=2: append 6 → [6]
93.  [I] CALL backtrack(2, [6], 1)
94.    [B] No  [E] No
95.    [G,H] i=2: append 6 → [6,6]
96.    [I] CALL backtrack(2,...,-5) → [E][F] dead
97.    [J] pop → [6]
98.    [G,H] i=3: append 7 → [6,7]
99.    [I] CALL backtrack(3,...,-6) → [E][F] dead
100.   [J] pop → [6]
101.   loop (G) exhausted → return to step1's call
102. [J] pop → []
103. [G,H] i=3: append 7 → [7]
104. [I] CALL backtrack(3, [7], 0)
105.   [B] remaining==0? YES → [C] SAVE [7]
106.   [D] return
107. [J] pop → []
108. loop (G) exhausted → return — ALGORITHM COMPLETE

FINAL RESULT: [[2,2,3], [7]]
'''