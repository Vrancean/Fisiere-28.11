with open('D:Input.txt','r') as f:
    l1=f.readlines()
print('Nr      Numele      Prenumele    Nota1 Nota2 Nota3\n')
print(*l1)
with open('D:CopieR.txt','w') as f:
    for n in l1:
        f.write(n)
for n in l1:
    l2=n.split()
    x=l2[0]+'   '+l2[1]+'   '+l2[2]
    media=str(round((float(l2[3])+float(l2[4])+float(l2[5]))/3, 2))
    y=x+'   '+media+'\n'
    with open('D:Output.txt','a') as f:
        f.write(y)
with open('D:Output.txt','r') as f:
    l3=f.readlines()
print('Nr      Numele     Prenumele      Media\n')
print(*l3)