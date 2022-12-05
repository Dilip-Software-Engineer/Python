'''
sum=0
for i in range(20,0,-2): 
     sum=sum+i 
     print(i)
     if i==14:
        continue
print(sum)
'''

sum=0
for i in range(20,0,-2):
    sum=sum+i
    print(i) 
    if i==14 :
        break
print(sum)