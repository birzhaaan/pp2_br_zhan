def un(nums):
    mas = []
    for i in nums:
        if i not in mas:
            mas.append(i)
    return mas

arr = [1,6,8,9,4,5,2,1,5]
arr1 = un(arr)
print(arr1)