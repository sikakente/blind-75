class Solution:
    def climb_stairs(self, n: int) -> int:
        """_summary_

        Args:
            n (int): _description_

        Returns:
            int: _description_
        """
        cache = {}

        def climb(step):
            if step in cache:
                return cache[step]
            if step == 1:
                return 1
            if step == 2:
                return 2

            cache[step] = climb(step - 1) + climb(step - 2)
            return cache[step]

        return climb(n)
