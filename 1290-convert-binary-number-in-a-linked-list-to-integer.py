
def getDecimalValue():
    binary = ['0', 'b']
    binary.append("1")
    binary.append("0")
    binary.append("1")
    print(binary)
    s = "".join(binary)
    print(s)
    result = int(s, base=2)
    print(result)


getDecimalValue()