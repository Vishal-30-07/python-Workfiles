y=list()

x=["nirmal","vishal",12,21,32,21,12,"nirmal"]
x[0]=9

# mutable-changeable
# it is ordered
# it allows duplicate

# x[0]
# x[6]
# x[7]

# append (append() is a built-in method of the list object used to add a single element to the end of an existing list)
name_1=["python","figma"]
name_1.append("flutter")

name_2=[1,2,3]
name_2.append(4)

name_3=["python",1,2,3,4,"figma"]
name_3.append([5,6])

# clear(remove all elements from the list, effectively making it an empty lis)
name_4=["python","figma"]
name_4.clear()

# count( It is used to determine the number of times a specified element appears within the list)
name_5=["python","figma","python"]
name_5.count("python")

# index(efers to the position of an element within a list)
name_6=["python","figma","python","figma"]
name_6.index("figma")
name_6[2]

# pop(removes an item at the specified index from the list)
name_7=["python","figma","canva","flutter"]
name_7.pop(3)
name_7.pop() #f no index is provided, pop() removes and returns the last element of the list by default.

# reverse (reverses the list in place)
name_7=["python","figma","canva","flutter"]
name_7.reverse()

# sort(organizes the elements of a list in ascending or descending order)
name_8=["python","figma","canva","flutter"]
name_8.sort()
name_9=[1,3,5,7,9,2,4,6,8]
name_9.sort()
name_9=[1,3,5,7,9,2,4,6,8]
name_9.sort(reverse=True)

# split(splits a string into a list)
mystring="hello world"
mylist=mystring.split()

# insert(a list method that allows you to add a single element to a specific position in the list)
x=["python","figma","canva","flutter"]
x.insert(2,"vishal")

# copy(powerful data structures used to store a collection of items)
x=["python","figma","canva","flutter"]
y=x.copy()
y

# insert,remove,extend,copy,append
# remove(removes the first occurrence of the element with the specified value)
x=["vishal",1,2,3,4,5,6,7,8,9]
x.remove("vishal")
x.remove(2)

# extend( a list method that adds elements from an iterable (like a list, tuple, or set) to the end of the existing list)
x=[1,2,3,4,5]
y=[6,7,8,9,10]
x.extend(y)
x

