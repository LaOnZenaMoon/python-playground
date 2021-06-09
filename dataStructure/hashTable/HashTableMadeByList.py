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

hash_table2 = list([0 for i in range(8)])

def saveDataUsingChaining(data, value):
    index_key = getKey(data)
    hash_address = hashFunction(index_key)

    if hash_table2[hash_address] != 0:
        for index in range(hash_address, len(hash_table2)):
            if hash_table2[index] == 0:
                hash_table2[index] = [index_key, value]
                return
            elif hash_table2[index][0] == index_key:
                hash_table2[index][1] = value
                return
    else:
        hash_table2[hash_address] = [index_key, value]

def readDataUsingChaining(data):
    index_key = getKey(data)
    hash_address = hashFunction(index_key)

    if hash_table2[hash_address] != 0:
        for index in range(hash_address, len(hash_table2)):
            if hash_table2[index] == 0:
                return None
            elif hash_table2[index][0] == index_key:
                return hash_table2[index][1]
    else:
        return None


print(hash_table)

saveData('dave', '0120123123')
saveData('andy', '0120123123')
print(readData('andy'))

print(hash_table)


print (hash('Dd') % 8)
print (hash('dc') % 8)

saveDataUsingChaining('Dd', '01012341234')
saveDataUsingChaining('dc', '01011111')

print(hash_table2)

print(readDataUsingChaining('Dd'))

print(hash_table2)