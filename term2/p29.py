a=["red","green","blue"]
#قراره از کاربر ۳بار سوال بپرسیم
javab1=input("رنگ مورد علاقه اول")
javab2=input("رنگ مورد علاقه دوم")
javab3=input("رنگ مورد علاقه سوم")
# چاپ لیست قبلی
print(a)
# اضافه کردن جواب ها به لیست
a.append(javab1)
a.append(javab2)
a.append(javab3)
#چاپ لیست جدید
print(a)