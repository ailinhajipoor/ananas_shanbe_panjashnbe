def jam(a,b):
    print(a+b)
def tafrigh(a,b):
    print(a-b)
def zarb(a,b):
    print(a*b)

a=int(input("adad bede"))
b=int(input("adad bede"))
c=input("alamat bede")
if c=="+":
    jam(a,b)
elif c=="-":
    tafrigh(a,b)
elif c=="*":
    zarb(a,b)
else:
    print("no motabar")
