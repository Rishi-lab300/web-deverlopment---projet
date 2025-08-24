text = input("Enter the string : ")
def non_repeating_characters(s):
    freq = {} 
    for ch in s:
        freq[ch] =freq.get(ch,0)+1
    print("Non repeating characters are: ")    
    for ch in s:
        if freq[ch]==1:
            print(ch , end ="") 
            print()

non_repeating_characters(text)                