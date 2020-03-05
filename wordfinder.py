s = raw_input()
C = raw_input()
c= raw_input()
NumC = 0
numc = 0
for i in range ( 1, len(s)-1):
    if s[i-1:i+len(C)-1] == C: #need to genralise i more. could ask user what they want to search in a text body
        NumC +=1
    if s[i-1: i+len(c)-1] == c:
        numc += 1
        
print '1st word frquency = ', NumC
print '2nd word frquency = ', numc