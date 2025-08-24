num = int(input("Enter number : " ))
sq = num * num
divider = 1
while divider<=num :
    divider *= 10
    
    
right = sq % divider
left = sq // divider
sum = left + right
if sum == num:
    print(num, "is a kaprekar number....")
else:
    print(num, "is not a kaprekar number....")    