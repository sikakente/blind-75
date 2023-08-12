class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = (numerator / denominator) < 0
        numerator = numerator * -1 if numerator < 0 else numerator
        denominator = denominator * -1 if denominator < 0 else denominator

        result = []
        quotient = numerator // denominator
        remainder = (numerator % denominator) * 10
        result.append(str(quotient))

        if remainder:
            result.append(".")
        else:
            if is_negative:
                result = ["-"] + result
            return "".join(result)

        idx = len(result)

        checker = {}

        while remainder:
            if remainder in checker:
                start_index = checker[remainder]
                recurring = result[:start_index] + \
                    ["("] + result[start_index:] + [")"]
                recurring = "".join(recurring)
                if is_negative:
                    return "-" + recurring
                return recurring
            quotient = remainder // denominator
            result.append(str(quotient))
            checker[remainder] = idx
            remainder = (remainder % denominator) * 10
            idx += 1

        if is_negative:
            result = ["-"] + result
        return "".join(result)
