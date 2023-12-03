# 1

# day_off = input("Do you have day off(yes/no)?  ").lower()
# vacation = input("Do you have vacation(yes/no)?  ").lower()
#
# if day_off == "yes":
#     day_off = True
# if day_off == "no":
#     day_off = False
#
# if vacation == "yes":
#     vacation = True
# if vacation == "no":
#     vacation = False
#
# if day_off or vacation:
#     print("You can sleep yet.")
# elif not (day_off or vacation):
#     print("Get up. You have to go to work.")

# 2


# num = int(input("Please, enter the number: "))
#
# if num < 21:
#     num1 = 21 - num
#     print(f"{num} -> {num1}")
# else:
#     num1 = (num - 21) * 2
#     print(f"{num} -> {num1}")


# 3
#
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
#
# res = number1 - number2
#
# if res < 0:
#     res = -res
# if res <= 100:
#     print(f"{number1} {number2} -> good")
# else:
#     print(f"{number1} {number2} -> bad")


# 4

# string = input("Write any text: ")
# cut_num = int(input("Enter the number of symbol you need to cut: "))
#
# res_str = string[:(cut_num - 1)] + string[cut_num:]
#
# print(res_str)


# 5

# switch_1 = input("Is the switch 1 on? yes/no: ").lower()
# switch_2 = input("Is the switch 2 on? yes/no: ").lower()
#
# if switch_1 == "yes":
#     switch_1 = True
# if switch_1 == "no":
#     switch_1 = False
#
# if switch_2 == "yes":
#     switch_2 = True
# if switch_2 == "no":
#     switch_2 = False
#
# if (switch_2 is True and switch_1 is True) or (switch_2 is False and switch_1 is False):
#     print("Excellent!!!")
# else:
#     print("It's bad :(")

# 6


# my_str = input("Write any text, please: ")
#
# result = my_str[-1] + my_str[:-1]
# print(result)


#  7

# num_1 = int(input("Please, enter number 1: "))
# num_2 = int(input("Please, enter number 2: "))
#
# if num_1 == num_2:
#     result = (num_1 + num_2) ** 2
# else:
#     result = num_1 + num_2
#
# print(f"{num_1} {num_2} -> {result} ")

# 8

# sec = int(input("Enter the time in seconds: "))
#
# d = sec // 3600 // 24
# h = (sec - d * 3600 * 24) // 3600
# m = (sec - d * 3600 * 24 - h * 3600) // 60
# s = (sec - d * 3600 * 24 - h * 3600 - m * 60)
#
#
# print(f"{d}:{h:02}:{m:02}:{s:02}")
