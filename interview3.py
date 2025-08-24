'''ch1 = input("Enter the first character : ")
ch2 = input("Enter the second character : ")
def check_frequency(s,d):
    freq1 = {}
    freq2 = {}
    for char in s:
        freq1[char] =freq1.get(char,0)+1 
        
    for char in d:
        freq2[char] =freq2.get(char,0)+1 
        
        
    if freq1==freq2:
        print("The given two string is an Anagram ")  
    else:
        print("the given strings is not an Anagram")   
     
     
check_frequency(ch1,ch2)
'''   
from collections import Counter
def freq_count(s,d):
    if Counter(s) == Counter(d):
        print("The given strings are anagram")
    else:
        print("The given strings are not anagrams.")
        
ch1 = input("Enter the first character : ")
ch2 = input("Enter the second character : ")
freq_count(ch1,ch2)        
            
    
       
    