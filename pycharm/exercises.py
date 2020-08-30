#上课
import time
time1 = time.ctime()
t1 = time.time()
year = int(input("输入年份："))
month = int(input("输入月份："))
day = int(input("输入日期："))


#啦啦啦啦啦阿拉



list_month1 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
list_month2 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
n = 0
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    for i,j in list_month1.items():
        if month > i:
            n += j
    n += day
else:
    for i,j in list_month2.items():
        if month > i:
            n += j
    n += day

#456789
print(n)
time2 = time.ctime()
t2 = time.time()
print(time1)
print(time2)
print(t2-t1)
#123456
