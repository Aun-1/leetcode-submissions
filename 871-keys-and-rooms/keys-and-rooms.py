from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue=deque([0])
        visited = {0}

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)

        # done = [False]*len(rooms)

        # def changeDone(idx): 
        #     if done[idx]:           # stop: already visited
        #         return
        #     done[idx] = True

        #     for i in rooms[idx]:
        #         changeDone(i)
        
        # changeDone(0)
        # for element in done:
        #     if element == False:
        #         return False
        # return True

