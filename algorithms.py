#Бинарный поиск 
def binary_search(nums, target):
    r, l = 0, len(nums) - 1
    while r <= l:
        m = (r + l) // 2
        if nums[m] == target: return m
        elif nums[m] > target: l = m - 1
        else: r = m + 1
    return -1

#Префиксные суммы
def prefixSum(arr):
    pref = [0] * (len(arr))
    pref[0] = arr[0]
    for i in range(1, len(arr)):
        pref[i] = pref[i - 1] + arr[i]
    return pref
