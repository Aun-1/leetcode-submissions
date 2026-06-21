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
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            root = parts[0]
            for file_info in parts[1:]:
                name, content = file_info.split('(')
                content = content[:-1]          # drop trailing ')'
                content_to_paths[content].append(root + '/' + name)

        return [group for group in content_to_paths.values() if len(group) > 1]