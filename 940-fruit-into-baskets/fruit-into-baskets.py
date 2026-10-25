class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        maxFruit=0
        fruitType={}

        for right in range(len(fruits)):

            if fruits[right] in fruitType:
                fruitType[fruits[right]]+=1
            else:
                fruitType[fruits[right]]=1

            while len(fruitType)>2:
                if fruitType[fruits[left]]>1:
                    fruitType[fruits[left]]-=1
                else:
                    del fruitType[fruits[left]]
                    
                left+=1

            maxFruit=max(maxFruit, right-left+1)

        return maxFruit
        '''
can only travel left to rgiht 
fruits[i] arr and each element tells type of fruit 
1 have two basckets and eahc cn only have 1 type of fruit 
one i reacha  tree that cannor fit the fruit into my basket, i mst stop 

-> return max i can pic 
        '''

'''
since we are looking for a ocitngiou array wti only 2diff numbers, 
we will use a dynamic sliding iwndow

for loop contorilling right poitner 

left pointer cntrolle by while loop 
the whikle loop consnditon will be based on if out set len has greatar than 2 

'''