#!/usr/bin/env python3
import sys
import re

#given n inputs
#print n+1
def main():
    threshold=float(input("threshold:"))
    limit=float(input("limit:"))
    nums=[]
    total=0
    for line in sys.stdin:
        if 'q'==line.rstrip():
            break
            #print(f'Input : {line}')
        value=compareThreshold(float(line), threshold)
        print(value)
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