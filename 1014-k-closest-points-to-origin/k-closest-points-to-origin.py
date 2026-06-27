class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sorted() takes:the list to sort///key= a function that it runs on every element to decide the order
        def distance(point):
            return point[0]**2 + point[1]**2
        
        sorted_points = sorted(points, key=distance)
        
        return sorted_points[:k]




        # distance={}
        # for i in points:
        #     distance[i[0]**2+i[1]**2]=points
        # count=0
        # result=[]
        # for dist, points in sorted(distance.items(), key=lambda x: -x[0]):
        #     result.append(points)
        #     count+=1
        #     if count==k:
        #         return result