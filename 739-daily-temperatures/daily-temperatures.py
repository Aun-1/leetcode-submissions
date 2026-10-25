'''
make an output arr of legnth eual to temp -> starting all 0
iterate from end-1 of tmp arry to 0 prev element stored
if end prev qa less than curr -> do nothing 
id if prev greater then use variable we incremnt in by 1 and repace elemtn with that 
'''
'''
naivre approach 
2 pointers 
the left poitner cntrolled by a for loop 
and right while greater temp found --> if it ecneeds length put 0 tere

'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []  # indices still waiting for a warmer day

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)

        return output
        # output = [0]*len(temperatures)
        # right=0
        # for left in range(len(temperatures)-1):
        #     found=False
        #     right=left+1
        #     while found is False:
        #         if temperatures[right]>temperatures[left]:
        #             output[left]=right-left
        #             found=True
        #         if right==len(temperatures)-1:
        #             found=True
        #         right+=1
        # return output