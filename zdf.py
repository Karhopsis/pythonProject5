
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor = xor ^ num
        print(xor)
    return xor

print(singleNumber([1,4,4,5,5,2,2]))