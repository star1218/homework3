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
#
#range(5)->5-1 =>4
#range(4)->4-1=>3
#range(3)->3-1=>2
#range(2)->2-1=>1


numbers1=int(input("Ведите число А: ")) #завд 3
numbers2=int(input("Ведите число Б:"))
def numbers_range(numbers1,numbers2):
    if numbers1==numbers2:
        return numbers1
    else:
        return numbers1+numbers_range(numbers1+1,numbers2)
print(numbers_range(numbers1,numbers2))

#numbers1(1) - numbers2(5) -> 1-5
#numbers1(2)-numbers2(5) ->2-5
#numbers1(3)-numbers2(5)->3-5
#numbers1(4)-numbers2(5)->4-5
#numbers1(5)-numbers2(5)->5-5
#1+2+3+4+5 (диапазон от 1 до 5)

