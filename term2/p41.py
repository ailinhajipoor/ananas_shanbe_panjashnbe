from random import choice
names=[]
for i in range(4):
    a=input("type your name : ")
    names.append(a)

print(names)
print(choice(names))
