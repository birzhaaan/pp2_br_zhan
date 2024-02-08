def spy_game(nums):
    massiv = [0,0,7]
    massiv_index = 0

    for num in nums:
        if num==massiv[massiv_index]:
            massiv_index+=1
            if(massiv_index == len(massiv)):
                return True
    return False
    
print(spy_game([1,2,3,4]))
print(spy_game([3,3,5,0,0,7]))
print(spy_game([3,0,5,5,0,5,7]))