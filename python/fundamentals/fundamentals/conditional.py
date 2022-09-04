a = 1
b = 2
if a < b:
    print("a is less than b") #must indent 4 lines

c = 4
d = 3 
if c < d:
    print("c is less than d") # will not print due to c being greater than d


e = 4
f = 3
if e < f:
    print("e is less than f") #will not print due to it being flase
else:
    print("e is no less than f") # will print due to it being true
print("outside the if statement") # will print due to being outside the print value

g = 9
h = 8
if g < h:
    print("g is less than h")
elif g == h:
    print("g is equal to h")
else:
    print("g is greater than h")

i = 20
j = 8
if i < j:
    print("i is less than j")
elif i > j + 10:
    print("i is greater than f by more then 10")
else:
    print("i is greater than j")
    

# BMI calculator 

name = "Bernard"
hieght_m = 2
weight_kg = 113

bmi = weight_kg / (hieght_m ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overwieght")
else:
    print(name)
    print("is overweight")


age = 20

if age > 18:
    print("can drive")
elif age < 18:
    print("cant drive")
else:
    print("not yet old enough")

