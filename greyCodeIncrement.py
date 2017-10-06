import argparse
from collections import deque

def get_input():
    parser = argparse.ArgumentParser()

    parser.add_argument('greyC')
    arg = parser.parse_args()
    list1 = arg.greyC
    return list1

def add_one(binCode):
    spot = len(binCode) - 1
    carry = 0
    cSum = 0
    one = [0,0,0,1]
    nextBin = deque()

    while(spot >= 0):
        cSum = carry + one[spot] + int(binCode[spot])
        if cSum == 3:
            nextBin.appendleft(1)
            carry = 1
        elif cSum == 2:
            nextBin.appendleft(0)
            carry = 1
        elif cSum == 1:
            nextBin.appendleft(1)
            carry = 0
        elif cSum == 0:
            nextBin.appendleft(0)
            carry = 0
        if(spot == 0):
            break
        spot -= 1
    return list(nextBin)


def increment(code):
    length = len(code)
    newBin = []   # will hold binary from grey
    nextBin = []  # will hold incremented binary
    newGrey = []        # will hold incremented grey
    newBin.append(code[0])
    for bit in range(length-1):
        if(newBin[bit] != code[bit+1]):
            newBin.append('1')
        else:
            newBin.append('0')
    nextBin = add_one(newBin)

    newGrey.append(nextBin[0])
    for bit in range(length-1):
        if(nextBin[bit] != nextBin[bit+1]):
            newGrey.append('1')
        else:
            newGrey.append('0')

    return newGrey


def main():
    greyC = get_input()
    result = increment(greyC)
    result = ''.join(map(str, result))
    print("Next grey code: ", result)



if __name__ == '__main__':
    main()
