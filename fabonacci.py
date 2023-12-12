n=int(input("enter no:"))
print("num---",n)
n1=0
n2=1
l=[]
print(n1)
print(n2)
num=n
s=0
l.append(n1)
l.append(n2)
nt=n1+n2
while nt < n:
    print(nt)
    l.append(nt)
    n1=n2
    n2=nt
    nt=n1+n2
for i in l:
    s=s+i
print("sum---",s)




