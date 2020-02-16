
def findNumbers(arr):
    total = 0
    for e in arr:
        s = str(e)
        if len(s) % 2 == 0:
            total += 1
    return total

print(findNumbers([12,345,2,6,7896]))
