with open ('D:assq.txt','r') as f:
    a=f.read()
v=[]
n=0
for i in range(0,len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
        n+=1
        v.extend(a[i])
print('Numarul de vocale este:',n)
print('Vocalele sunt:',v)