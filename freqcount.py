with open("data.txt" , "r")as f:
    line=f.read()
    
    words = line.split()
     
freq = {}
for word in words:
    if word in freq:
        freq[word] +=1
    else:
        freq[word] =1   
sorted_freq = sorted(freq.items() ,key = lambda  x: x[1] , reverse =True)    

for word , count in sorted_freq[:5]:
    print(word , " :",count)         
    
    