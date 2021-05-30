# Courses
# Login/Signup
# Question 6
# Question 6

# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function speed naam ka ek parameter lega. 1. Agar speed 
# 70 se kam hai to ye “ok” print karega.

#     Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point dega (ye 70 ko count nahi karega).

#     example ke liye agar speed 80 hai to print karega “points:2” .

#     Agar driver ko 12 points se jyaada points milte hai to , function “License suspended” print karega


def driver_speed(speed):
    if range_of_speed<=70:
        print("ok")
    elif range_of_speed>70:
        a=speed-70
        print(a)
        if b==0:
           print(a//5,"point")
           if a>12:
            print(a//5,"point")
            if a>12:
                print("license suspended")
range_of_speed=int(input("enter the speed:"))
driver_speed(range_of_speed)