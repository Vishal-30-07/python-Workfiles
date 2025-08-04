# dict
# a mutable collection of key-value pairs that allows for efficient data retrieval using unique keys
# key-value` pairs storing type

dict_1={}
dict_2=dict()

dict_3={"key":2,}
print(dict_3["key"])

dict_4={1:1,"list1":[1,2,22,1,]}
print(dict_4[1])
print(dict_4['list1'])

# clear( erase all contents of the dictionary)
dict_4={1:1,"list1":[1,2,22,1,]}
dict_4.clear()

# copy(a straightforward way to make a shallow copy of a dictionary)
dict_4={1:1,"list1":[1,2,22,1,]}
dict_5=dict_4.copy()
print(dict_5)

# fromKeys (generates a new dictionary from the specified sequence of elements as keys and a user-supplied value)
dict_5={'item_1','item_2','item_3'}
dict_6= dict.fromkeys(dict_4)
print(dict_1)

dict_5={'item_1','item_2','item_3'}
dict_1={'hi'}
dict_6= dict.fromkeys(dict_4,dict_1)

# get(returns the value of the key if the key is present in the dictionary)
dict_4.get("list1")
dict_4["list1"]
dict_4={1:1,"list1":[1,2,22,1,],"name":"nirmal"}

value=dict_4.items()
value2=list(value)
# value2[1][1][1]

dict_4.keys()
dict_4.pop(1)

dict_4.popitem()

dict_4={1:1,"list1":[1,2,22,1,],"name":"nirmal"}
dict_4.update({2:1})
dict_5={5:1,"list2":[1,2,22,1,]}
dict_4.update(dict_5)
dict_4.update({5:2})


dict_4.values()
dict_4.items()
dict_4.keys()

dict_4.setdefault("name","nirmal")
dict_4["list3"]
dict_4.get("list3")
dict_4.setdefault("list2","nirmal")



















