# # Inner Function
# Python Inner Functions

# Ek function jo ki kisi dusre function ke andar likha jaata hai ya define kiya jaata hai use inner function ya nested function 
# kehte hai. Inner functions, outer function ke scope ke variables Ko access kar sakta hai lekin unn variables ko change nahi kar 
# sakta hai. EXAMPLE:-
 
# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()

# f1() 




# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function()




def first_function():
    s='I love India'
    def second_function():
        s="MY NAME IS JACK"
        print(s)     
    second_function()
    print(s)
first_function() 