def spy_game(nums):
    nums=list()
    for i in range(len(nums)):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7 :
            return True
    return False

if spy_game([1,7,2,0,4,5,0])== True:
    print("True")
else:
    print("False")