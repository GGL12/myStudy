class Sulotion:
    def last_remaining_solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        value = 0
        for index in range(2, n+1):
            current_value = (value + m) % index
            value = current_value
        return value