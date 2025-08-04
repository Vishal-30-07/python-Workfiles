# Arithmetic operators
from traceback import print_tb

a=6
b=6

# add
print(a+b)

# Sub
print(b-a)

# multiply
print(a*b)

# division
print(a/b)

# floor division
print(a//b)

# exponent

print(a**b)

a=10
b=11
# remainder/modulus
print(a%b)

name_1="nirmal"
name_2="nirmal"

if(name_1):
    print(name_1)


# assignment operator

# +=

a=5
a=a+5
a
a+=6
a=5

list_1=[1,1]
# list_1[10]
print(a)

a=8
a-=6
a/=2
a*=2
a**=2
a//=2
a
a=10
a%=5
a&=3
a|=3

a=10
a>>=3
a<<=3
if(x:=5):
    print("nirmal")
# xor operator

x=5
x^=3
x

x=5
y=6
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<y)
print(x>=y)
print(x<=y)

# logical operator

x=5
y=10
print(x==5 and y<=6)
print(x==6 or x<6)
print(not(x==5))


# identity operator

x=["nirmal"]
y=x.copy()
print(x is y)
y=["nirmal"]
print(x==y)

# -5 to 256
x=256
y=256
print(x is y)
x=256
y=x
print(x is not y)

x="Nirmal"
y="i"
print(y in x)
print(x in y)
print(y not in x)

# membership operator

x=[[1,2],3,4]
y=3
print(y in x)

# bitwise operator
x=5
y=6
print(x&y)

