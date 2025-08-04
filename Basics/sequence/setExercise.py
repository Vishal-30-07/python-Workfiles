# set immutable
#set unordered
# duplicates not allowed

x=set((1,2,3))
x

# add(add a specific ele  ment into a Set collection)
x=set([1,2,3])
x={1,2,3,4,5,6}
x.add(8)
x={1,2,3,4,5,6}
x.add(4) #it does not allow duplicate
x={1,2,2,2,3,4,4}
x.add(3)

# remove(used to remove the elements from the lists)
x={1,2,2,3,33,2,2,22,2,44,2,2,2,22,33,222,22,}
x.remove(3)
type(x)
x={1,2,3,3,3,3,4}
x
x.remove(3)
x.add("vishal")

# clear(removes all elements from this set)
x={1,2,3,3,3,3,4}
x.clear()

# copy( returns a shallow copy of a specified set)
x={1,2,3,3,3,3,4}
y=x.copy()
y

# Pop( removes a random item from the set)
x={1,2,3,3,3,3,4}
x.pop()

# difference(function returns the difference between two or more sets)
x={1,2,3}
y={2,3,4}
x.difference(y)
x={'vishal','nirmal',4,5}
y={'python',3,4,'vishal'}
x.difference(y)

#difference_update( modifies a set by removing all elements present in another set,
# keeping only the ones that are not found in the other one)

x={1,2,3,3,2,1}
y={5,4,3}
x.difference(y)
x
x.difference_update(y)

# discard(removes the specified item from the set)
x={1,2,3,3,2,1}
x.discard(1)

# remove check for the value it the value is in the set remove it or no error will be returned
x.discard(1)
# remove check for the value it the value is in the set remove it or else returns error
x.remove(2)
x.discard(2)

# intersection(the set that contains all the elements that are common to both sets)

x={1,2,3,4}
y={4,3,5}
x.intersection(y)

# intersection_update(the intersection() method returns a new set, without the unwanted items,
# and the intersection_update() method removes the unwanted items from the original set)

x={1,2,3,4}
y={1,3,2}
x.intersection_update(y)

# issubset(returns True if all items in the set exists in the specified set, otherwise it returns False)
x={1,2,5}
y={1,3,2,4}
x.issubset(y)

x={1,2,5}
y={1,3,2,4,5}
x.issubset(y)

# issuperset(returns True if all items in the specified set exists in the original set, otherwise it returns False)
x={1,3,2,4,5}
y={1,2}
x.issuperset(y)

x={1,2,5}
y={1,3,2,4,5}
x.issubset(y)

# isdisjoint(efficiently determines whether two sets have no elements in common, that is, if they are disjoint)
x = {2,5}
y = {1, 3, 2, 4}
x.isdisjoint(y)

y = {1, 3, 2, 4}
x = {2,5}
x.isdisjoint(y)

x = {0,5}
y = {1,2,3,4}
x.isdisjoint(y)

# symmetric difference(it removes the coman values on both set)
x = {5,1,2,3}
y = {1, 3, 2, 4}
x.symmetric_difference(y)

x = {1,2,3,4}
y = {5,6,7,8}
x.symmetric_difference(y)

# symmetric difference update(updates the original set by removing items
# that are present in both sets, and inserting the other items)

x = {1,2,3,4}
y = {5,6,7,8}
x.symmetric_difference_update(y)

# union(to combine multiple sets into a single set, containing all unique elements from the given sets)
x={1,2,3,3}
y={1,2,4}
x.union(y)

x={1,2,3,4}
y={5,6,7,8}
x.union(y)

# update( updates the current set, by adding items from another set)
x={1,2,3,3}
y={1,2,4}
x.update(y)

