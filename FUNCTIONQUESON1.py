
def count_number():
    list1=[1,2,3,2,2,1,3,3,3]
    i=0
    a=[]
    b=[]
    while i<len(list1):
        count=0
        m=list1[i]
        j=0
        while j<len(list1):
            n=list1[j]
            if m==n:
                b.append(n)
                count=count+1
            j=j+1
        k=0
        while k<len(list1):
            if m not in a:
                a.append(m)
                print(m,"=",count)
            k=k+1
        i=i+1
count_number()