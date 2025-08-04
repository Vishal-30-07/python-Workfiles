
# loops(sed to repeat a specific block of code a known number of times)

# for loop(used to iterate over a sequence (like a list, tuple or string) or other iterable objects)

# while loop(a control flow statement that allows code to be executed repeatedly,
# depending on whether a condition is satisfied or not)

for i in range(10):
    print('vishal')

for i in range(0,10): #range(initial,final)
    print(i)

for i in range(0, 10,2): #range(initial,final,step)
        print(i)

i=0
while i<15:
    print(i)
    i+=1

for i in range(0,10):
    if i==5:
        continue
    print(i)

for i in range(0,10):
    if i==5:
        continue
    print(i)
else:
    print('end')

i=20
while i>10:
    print(i)
    i+=1
    if i==i:
        break
    print('vishal')

