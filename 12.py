c = 0
string = input()
sub_string = input()
l = len(sub_string)
i=0
j=0
while i<len(string):
    while j<l:
        if string[i]==sub_string[j]:
            i+=1
            j+=1
            if j==l:
                c+=1
        else:
            j=0
            i+=1
            
print(c)
    
