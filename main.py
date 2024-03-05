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

# number=int(input("Ведите число N:")) #завд 2
#
# def star(number):
#     if number>0:
#         print("*",end="")
#         star(number-1)
#     else:
#         print()
# star(number)

numbers1 = int(input("Ведите число А: "))
numbers2 = int(input("Ведите число Б:"))
def numbers_range(numbers1, numbers2):
    if numbers1==numbers2:
        return numbers1
    else:
        return numbers1 + numbers_range(numbers1 + 1,numbers2)
print(numbers_range(numbers1,numbers2))



