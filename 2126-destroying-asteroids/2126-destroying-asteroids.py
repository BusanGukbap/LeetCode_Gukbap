class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        print(asteroids)

        temp = list()

        n = len(asteroids)
        temp.append(mass)
        for i in range(n):
            if temp[-1] < asteroids[i]:
                return False
            
            temp.append(temp[-1] + asteroids[i])
        
        return True

            
        