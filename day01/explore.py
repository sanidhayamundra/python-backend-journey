a=[1,2,3]
b=a
b.append(4)
print("a:",a)
print("b:",b)
print(a is b,id(a),id(b))

c= a.copy()
c.append(99)
print(c,a is c, a==c)

x=10
print(type(x))

x="helloo"

print(type(x))


s = "hi"
print("id before:", id(s))
s += "!"
print("id after: ", id(s))   # different id → a NEW object was created


def modify(lst):
    lst.append("hii")

def assign(lst):
    lst=["hii00"]

lst=[1,2,3]
modify(lst)
print(lst)
assign(lst)
print(lst)

for i in lst:
    print(i)


a=input("enyter an no.")
b=input("enter another no.")
a=int(a)
b=int(b)

print(a+b,a/b,a//b,a%b,a**b)


list=[2,46,3,4,2444,34]

a=max(list)

print(a)


s="sanidhaya mundra"
map={}

for i in s:
    if i in map:
        map[i]+=1
    else:
        map[i]=1


print(map)


a1 = [1, 2]
b1 = a1
c1 = a1.copy()
b1.append(3)
print(a1, b1, c1)
print(a1 is b1, a1 is c1, a1 == c1)


s="hellooldleh"

def fun(s):
    return s==s[::-1]

print(fun(s))

