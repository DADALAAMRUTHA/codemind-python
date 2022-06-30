n=input()
k='aeiouAEIOU'

p='0123456789'
v=0
c=0
d=0
ws=0
for i in n:
    if i in k:
        v=v+1
    if i not in k and i not in p:
        c=c+1
    if i in p:
        d=d+1
    if ord(i)==32:
        ws=ws+1
print("Vowels:",v)      
print("Consonants:",c-ws)
print("Digits:",d)
print("White spaces:",ws)