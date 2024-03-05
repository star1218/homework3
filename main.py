# def my_pow(number, power): #завд 1
#     if power <= 1:
#         return number
#
#     return number * my_pow(number, power - 1)
#
#
# print(my_pow(2, 3))
#
# # my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# # my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# # my_pow(2, 1) => 2

number=int(input("Ведите число N:"))

def star(number):
    if number>0:
        print("*",end="")
        star(number-1)
    else:
        print()
star(number)
