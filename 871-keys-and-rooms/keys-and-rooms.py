'''


'''
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        done = [False]*len(rooms)

        def changeDone(idx): 
            if done[idx]:           # stop: already visited
                return
            done[idx] = True

            for i in rooms[idx]:
                changeDone(i)
        
        changeDone(0)
        for element in done:
            if element == False:
                return False
        return True