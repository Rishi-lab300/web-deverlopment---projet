nums = [1,2,2,3,4,5,5,6]

seen = set()

for num in nums:
    if num  in seen:
        print(num)
    seen.add(num)
        