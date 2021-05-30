#  Question 5
# Question 5

# Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke number jo ki 3 aur 5 ke multiples 
# hain unka sum print karega.jaisa ki niche dikhaya gya hai. Input:- 3 aur 5 ke multiples => 3, 5, 6, 9, 10 Output :-v


def number(a):
    limit=1
    sum=0
    while limit<=m:
        if limit%3==0 or limit%5==0:
            print(limit)
            sum=sum+limit
        limit=limit+1
    print(sum)
m=int(input("enter the number"))
number(m)

def expended_from(a):
    i=0