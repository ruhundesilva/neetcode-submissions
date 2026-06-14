class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = {}
        for i in range(len(position)):
            posSpeed[position[i]] = speed[i]
        
        position.sort()
        for i in range(len(position)):
            speed[i] = posSpeed[position[i]]
        
        time = []
        for i in range(len(position)):
            finish = (target - position[i]) / speed[i]
            time.append(finish)
        
        res = 1
        slowest = time.pop()
        while time:
            curr = time.pop()
            if curr > slowest:
                res += 1
                slowest = curr
        return res