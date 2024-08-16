nums=[7,3,4,45,6,7]
for i in range(len(nums)):
    if nums[i]%i==0:
        print(f"{i} not a prime number")
    else:
        print(f"{i} is a prime number")
