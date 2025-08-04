x=()
x=tuple()
x=(1,2,3,"Nirmal",3)
x
x[0]
x[0]=10
# it is immutable
# it is ordered
# it allows duplicates

# count(returns the number of times a specified value appears in the tuple)
x=(1,2,3,4,5,4,3,2,1,1,2,3)
x.count(2)
x=(1,2,3,"vishal","sanjay","vishal","sanjay")
x.count("vishal",2)

# index(a straightforward and efficient way to search for the
# first occurrence of a specified element and return its position)
x=("vishal","sanjay","nirmal")
x.index("vishal")