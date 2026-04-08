class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        we want to pair up each position and speed for the respective cars 
        sort them in decending order(closest to the target)
        get the time for each car
        add to the stack if greater than the previous time, as they took longer(another fleet)
        if equal or less than the previous time, they join the previous fleet as they cannot overtake
        """

        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)    