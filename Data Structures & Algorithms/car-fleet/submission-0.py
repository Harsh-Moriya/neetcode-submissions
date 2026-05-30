class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine the positions and speeds for easier access
        # Sorted in decending by position
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        stack = []

        for p, s in cars:
            # Get the time at which the car will reach target
            time_to_target = (target - p) / s
            stack.append(time_to_target)

            # Check if the current car (-1) is will reach the target in less or equal time as compared to the car ahead (-2)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)