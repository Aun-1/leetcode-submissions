class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        new_list = []
        for i in paths:             
            data = i.split()         
            new_list.append(data)

        for i in range(len(new_list)):
            root_info = new_list[i][0]
            for j in range(1, len(new_list[i])):
                name, content = new_list[i][j].split('(')   # O(k)
                key = content[:-1]                            # O(k)
                value = root_info + '/' + name                # O(k)
                res[key].append(value)

        sol = []
        for i in res:
            if len(res[i]) > 1:      
                sol.append(res[i])   
        return sol