#!/usr/bin/env python3
import sys

#given n inputs
#print n+1
def main():
    threshold=float(sys.argv[len(sys.argv)-2])
    limit=float(sys.argv[len(sys.argv)-1])
    nums=[]
    total=0
    INPUT_FILE = sys.argv[1]
    with open(INPUT_FILE, "r") as f:
        for line in f:
            value=compareThreshold(float(line), threshold)
            nums.append(value)
    for i in range(0, len(nums)):
        previous = total
        total = total + nums[i]
        if (total > (limit)):
            nums[i] = (limit) - previous
            total=limit
            setZero(i,nums)
            break
    for items in nums:
        print(items)
    print(total)


def compareThreshold(line,threshold):
    if(line>threshold):
        output=line-threshold
    else:
        output=0.0
    return output

def setZero(i,nums):
    for j in range(i+1, len(nums)):
        nums[j] = 0.0



if __name__ == "__main__":
    main()