mylist=[]
n=int(input(""))
k=int(input(""))
sum=0
for i in range(n):
    mylist.append(int(input()))
for i in range(k):
    sum=sum+mylist[i]
print(sum)  
