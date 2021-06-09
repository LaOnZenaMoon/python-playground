hash_table = list([0 for i in range(8)])

def getKey(data):
    return hash(data)


def hashFunction(key):
    return key % 8


def saveData(data, value):
    hashAddress = hashFunction(getKey(data))
    hash_table[hashAddress] = value


def readData(data):
    hashAddress = hashFunction(getKey(data))
    return hash_table[hashAddress]


print(hash_table)

saveData('dave', '0120123123')
saveData('andy', '0120123123')
print(readData('andy'))

print(hash_table)
