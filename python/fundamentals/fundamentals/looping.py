a = ["banana", "apple", "microsoft"]

for i in a: # i can be anything
    print(i)
    
for element in a:
    print(element)
    print(element)
    
b = [20, 10, 5]
for e in b:
    print(e)

c = [20, 10, 5]
total = 0
for e in b:
    total = total + e
print(total)

# 1, 2, 3, 4
c = list(range(1, 5))
print(c)

for i in range(1,5):
    print(i)
    
total2 = 0
for i in range(1,5):
    total2 += i
print(total2)


print(list(range(1,8)))

print(4 % 3)

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

#can you compute all multitples of 3,5 
# that are less than 100

for count in range(0,5):
    print("looping =", count)
    

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

