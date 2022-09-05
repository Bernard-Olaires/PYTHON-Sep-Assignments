#literal notation
person = {
    "first": "Ada", 
    "last": "Lovelace", 
    "age": 42, 
    "is_organ_donor": True
}

for key, value in person.items(): # creating a for loop keys in the dictionary
    print("key: ")
    print(key)
    print("value: ")
    print(value)
    print("")
    



# -- to delete key in dictionary -- 

del person["last"] 
value_removed = person.pop("age")
print(person)


print("------------------------") #gives space to output

# -- For loops and Dictionaries --

bernards_car = {
    "brand" : "Scion",
    "model" : "tC",
    "year" : 2013
}
print(bernards_car)

print("------------------------") #gives space to output

for each_key in bernards_car: 
    print(each_key)

print("------------------------") #gives space to output

for each_key in bernards_car:
    print(bernards_car[each_key])

print("------------------------") #gives space to output





capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}

# another way to iterate through the keys
for key in capitals.keys():
    print(key) 

# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values

print("------------------------") #gives space to output


for val in capitals.values():
    print(val)

# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values



print("------------------------") #gives space to output


for key, val in capitals.items():
    print(key, " = ", val)
    
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc




print("------------------------") #gives space to output




