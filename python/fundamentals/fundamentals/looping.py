# a = ["banana", "apple", "microsoft"]

# for i in a: # i can be anything
#     print(i)

# for element in a:
#     print(element)
#     print(element)

# b = [20, 10, 5]
# for e in b:
#     print(e)

# # how to sum up all numbers in c
# c = [20, 10, 5]
# total = 0
# for e in b:
#     total = total + e
# print(total)

# # how to outptu list range
# # [1, 2, 3, 4]
# c = list(range(1, 5))
# print(c)

# # how to output: 1, 2, 3, 4
# for i in range(1,5):
#     print(i)

# # how to sum up numbers
# total2 = 0
# for i in range(1,5):
#     total2 += i
# print(total2)


# # how to output [1, 2, 3, 4, 5, 6, 7]
# print(list(range(1,8)))


# # modulo operator 
# print(4 % 3)

# # example of modulo operator
# time = 67000
# hours = int(time/3600)
# minutes = int((time/60) % 60)
# seconds = 6700 % 60

# print(f"{time} seconds = {hours} hours, {minutes} minutes and {seconds} seconds")


# # modulo operator with odd 
# for number in range (10):
#     if(number % 2 != 0):
#         print(number)


# #can you compute all multitples of 3,5 
# # that are less than 100

# for count in range(0,5):
#     print("looping =", count)


# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# total3 = 0
# for i in range(1, 8):
#     if i % 3 == 0:
#         total3 += i
# print(total3)



myList = [1,2,3]

for i in range(0,len(myList)):
    print(i)
    # print(myList[i])