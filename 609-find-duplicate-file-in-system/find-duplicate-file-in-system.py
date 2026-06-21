class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # new_list=[]
        # for i in paths:
        #     data=i.split()
        #     new_list.append(data)

        # value_dict=[]
        # for i in range(len(new_list)):
        #     root_info=new_list[i][0]
        #     for j in range(1,len(new_list[i])):
        #         key=new_list[i][j][6:-1]
        #         value=root_info+'/'+new_list[i][j][:5]
        #         res[key].append(value)
        res = defaultdict(list)
        new_list = []
        for i in paths:              # O(P) iterations, P = number of paths
            data = i.split()         # O(L_i) - L_i = length of string i
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
            if len(res[i]) > 1:      # O(1) per check
                sol.append(res[i])   # O(1) amortized, but copies a list reference
        return sol