data = input().split()
x=int(data[0])-1
y=int(data[1])
day=0
for i in range(1,x+1):
	if i in [1,3,5,7,8,10]:
		day+=31
	elif i in [4,6,9,11]:
		day+=30
	elif i==2:
		day+=28
day+=y
weekDay=day%7
if weekDay==1:
	print("MON")
elif weekDay==2:
	print("TUE")
elif weekDay==3:
	print("WED")
elif weekDay==4:
	print("THU")
elif weekDay==5:
	print("FRI")
elif weekDay==6:
	print("SAT")
else:
	print("SUN")
