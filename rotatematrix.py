import numpy as np
arr = np.array([[10,20,30],
                [40,50,60]])
print(arr.T)
print(arr.T[: ,::-1])#90° rotation.
print(arr.T[::-1 ,:])#270° rotation.
print(arr.T[::-1,::-1])#180°
 
arr1 = np.random.randint(1,20,size=(6,6))
print(arr1)
top_left =arr1 [:3,:3]=0

print("top left :\n " , arr1)
bottom_rightt =arr1 [3:,3:]=1
print("bottom right : \n" , arr1)
n = arr1.shape[0]
mid = n//2
top_right = arr1[:mid,mid:]
print("Top right : \n" , top_right)
bottom_left = arr1[mid:,:mid]
print("bottom left : \n" , bottom_left)
