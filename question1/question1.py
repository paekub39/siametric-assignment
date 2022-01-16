
def remove_duplicates(num):
    pointer = 0
    current = None
    for val in range(len(num)):
        if current != num[val]:
            current = num[val]
            num[pointer] = current
            pointer = pointer + 1
    return pointer


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expectedNum = [0, 1, 2, 3, 4]
    k = remove_duplicates(nums)
    assert k == len(expectedNum)
    for i in range(k):
        assert nums[i] == expectedNum[i]
