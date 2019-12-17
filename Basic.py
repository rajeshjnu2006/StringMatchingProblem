'''Text = “aaabbccbcbcabababcbc”
Pattern = [“aba”, ”abab”, ”cbc”]

Output: 
aba: 2
abab: 2
cbc: 3

Answer B.1: 

Solution1: '''
       
text = "aaabbccbcbcabababcbc"   # Let length is n
patterns = ["aba", "abab", "cbc"] 
# Let the length of the list is m, and the length of the longest pattern is p
for pat in patterns: # m times
    count = 0 
    for i in range(len(text)-len(pat)+1): # n times
# p times slicing and p times comparison i.e. p+p = 2 p time
        if text[i:i+len(pat)] == pat:             
            count = count+1
    print("{}:{}".format(pat,count))

#Solution2: (Using dictionary avoiding p operations)

text = "aaabbccbcbcabababcbc"   # Let length is n
patterns = ["aba", "abab", "cbc"] 
# Let the length of the list is m, and the length of the longest pattern is p

for pat in patterns: # m times
    freq_dict = {pat:0}
    for i in range(len(text)-len(pat)+1): # n times
        if text[i:i+len(pat)] in freq_dict: # slicing is a p time operation
            freq_dict[pat]+=1
    print("{}:{}".format(pat,freq_dict[pat]))



#The above code will take O(m*n*p)
#Read this for better complexity algorithms (https://en.wikipedia.org/wiki/String-searching_algorithm)

#If all patterns in the “patterns” are of the same length it can be done in O(n*p) -- see below:


text = "aaabbccbcbcabababcbc"   # Let length is n
patterns = ["aba", "abb", "cbc"] 
# Let the length of the list is m, and length of the longest pattern is p
freq_dict = {}
for pat in patterns: # m times
    if pat not in freq_dict:
        freq_dict[pat] = 0
    
for i in range(len(text)-len(pat)+1): # n times
    curr_pattern = text[i:i+len(pat)]
    if curr_pattern in freq_dict: # slicing is a p time operation
        freq_dict[curr_pattern]+=1
     
for key in freq_dict: # just printing
    print("{}:{}".format(key, freq_dict[key])) 
