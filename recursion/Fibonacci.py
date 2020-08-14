class Fibonacci:

    def perform(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        returnValue = self.perform(n-1) + self.perform(n-2)
        return returnValue


fibonacci = Fibonacci()
for index in range(0, 10):
    print(fibonacci.perform(index))