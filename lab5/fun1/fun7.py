def has_33(nums):
    for i in range(len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
if has_33([1, 3, 3])==True:
    print("True")
else:
    print("False")

