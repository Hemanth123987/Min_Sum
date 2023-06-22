n,m=input().split()
n=int(n)
m=int(m)
l=[]
for i in range(n):
        num=input()
        num=num.split()
        l.append(num)
l2=[]
for i in l:
    sl=[]
    for j in range(len(i)):
        n1=int(i[j])
        sl.append(n1)
    l2.append(sl)
new_list=[]
for i in l2:
    mi=min(i)
    new_list.append(mi)
print(sum(new_list))