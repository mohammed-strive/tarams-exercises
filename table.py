import sys

def extract_table(rawData, noColumns):
    rawData = list(filter(bool, map(str.strip, rawData)))
    data = {} 
    for i in range(noColumns):
        slice = rawData[i::noColumns]
        data[slice[0]] = slice[1:]

    return data

with open(sys.argv[1], 'r') as fh:
    rawData = fh.readlines()
    print(extract_table(rawData, 3))
