class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = {}
        fleet = 1

        for i in range(len(position)):
            p = position[i]
            time = (target - p) / speed[i]
            times[p] = time
        
        position = sorted(position, reverse = True)
        maxTime = times[position[0]]

        for i in range(1, len(position)):
            p = position[i]
            if maxTime < times[p]:
                fleet += 1
                maxTime = times[p]

        return fleet