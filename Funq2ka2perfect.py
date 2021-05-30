# Courses
# Login/Signup
# Question 2
# Question 2

# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana hai ki vo perfect 
# number hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print 
# kare.[ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss 
# number ke barabar hota hai. Example:- Expected Output :


def perfect(a):
    num=a
    i=1
    sum=0
    while i<a:
        if a%i==0:
            sum=sum+1
        i=i+1
    if num==sum:
        print(num,"it is perfect")
    else:
        print(num,"it is not perfect")
n=int(input("enter the numbre"))
perfect(n)
