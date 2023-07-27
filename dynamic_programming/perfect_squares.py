class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        def get_perfect_squares():
            counter = 1
            squares = []
            current_square = 1

            while counter < n:
                current_square = counter * counter
                if current_square > n:
                    break
                squares.append(current_square)
                counter += 1

            return squares

        perfect_squares = get_perfect_squares()

        all_sums = [float("inf")] * (n+1)
        all_sums[0] = 0

        for perfect_square in perfect_squares:
            for target in range(1, n+1):
                difference = target - perfect_square
                if difference >= 0:
                    all_sums[target] = min(
                        all_sums[target], 1 + all_sums[difference])

        return -1 if all_sums[-1] == float("inf") else all_sums[-1]
