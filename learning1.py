print("<<<<<<<<<<<<<< STRING METHODS  >>>>>>>>>>>>>>>  ")
text = "Python is better than Java"
print("Original text : " , text)
print("Upper Case :" , text.upper())
print("Lower Case :" , text.lower())
print("Replaced text : " , text.replace("better" , "not better"))
print("Split text : " , text.split())
print("Join text : " , " launguage ".join(text.split()) )

print("/n <<<<<<<<<<<<<<< LIST METHODS >>>>>>>>>>>>>")
nums = [5,2,9]
print("Original nums : " , nums)
nums.append(7)
print("append :" , nums)
nums.insert(3,10)
print("insert:" , nums)
nums.pop()
print("pop : " , nums)
nums.remove(10)
print("Remove :" , nums)
nums.sort()
print("Sorted : " , nums)
nums.reverse()
print("reversed : " , nums)


print("/n <<<<<<<<<<<<<<< DICT METHODS >>>>>>>>>>>>>")
student = {"name" : "Rishi" , "Age" : 19 , "marks" : 100}
print("Keys :" ,  student.keys())
print("Values :" , student.values())
print("items : " , student.items())
print("Get age :" , student.get("Age"))
student.update({"city" : "Shajapur"})
print("Updated :" , student)
student.pop("marks")
print("AFter pop :" , student)

print("/n <<<<<<<<<<<<<<< SET METHODS >>>>>>>>>>>>>")
a = {1 , 2 , 3}
b = {4 , 5 , 6}
print("Union :" , a.union(b))
print("Intersection :" , a.intersection(b))
a.add(6)
print("ADD :" , a)
a.remove(2)
print("REmoved  :" , a)