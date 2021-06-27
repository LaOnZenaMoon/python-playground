def doFactorial(num):
    if num > 1:
        return num * doFactorial(num - 1)
    else:
        return num

print(doFactorial(10))
