# try, exept, finaly, else

# try:
#     input_num = int(input())
#     number = 13 / input_num
#     print(number)
# except:
#     print("Oops!")
# open('text.txt', 'r')
# try:
#     open('text.txt', 'r')
# except FileNotFoundError as err:
#     f = open('text.txt', 'a+')
#     # print(err)
#     for i in range(1, 101):
#         f.write(str(i))
#     f.seek(0)
#     print(f.read(), err)
#     f.close()


# import rando
# from random import randint, random
from random import *
# a = randint(1, 100)
# print(a)

# random_number = random()
# print(random_number)

# range_random =randrange(1,30)
# print(range_random)

# lists = ["apple", "banana", "pen", "octopus"]
# choices(lists)
# print(choices(lists, [6, 1, 1, 3], k=15))

f = open("text.txt", "r")
l = []
for line in f:
    l.append(line)
print(l)
# if len(l) % 2 == 0:
li = choices(l, k=2)
print(li)