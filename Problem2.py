a=[1,4,7,9,1,3,5,10,11]


for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        if a[i+1] <= a[i+2]:
            temp=a[i+2]
            a[i+2]=a[i+1]
            a[i+1]=temp

print(a)