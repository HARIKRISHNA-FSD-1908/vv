a=input()
s=""
for x in a:
    if x.isdigit():
        s=s+x
s=int(s)
sum=0;
while(s>0):
    sum=sum+(s%10)
    s=s//10
print(sum)    

