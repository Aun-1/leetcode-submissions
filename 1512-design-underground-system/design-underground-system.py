class UndergroundSystem:

    def __init__(self):
        self.checked_in = {} 
        self.trip_data = {} 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checked_in.pop(id)
        key = (startStation, stationName)
        if key not in self.trip_data:
            self.trip_data[key] = [0, 0]
        self.trip_data[key][0] += t - startTime
        self.trip_data[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trip_data[(startStation, endStation)]
        return total / count
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)