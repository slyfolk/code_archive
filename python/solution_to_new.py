def str_count(arg):
	trans = []
	c = []
	for i in arg:
		if i.isalpha() and not i in c:
			count = arg.count(i)
			result = i, count
			c.append(i)
			trans.append(result)
	trans.sort()
	print (trans)
	for i,j in trans:
		print(i,j)




def time():
	print("Enter the time with two digits separated by a (:) in this format \n 12hr format '07:49:51 AM'\n 24hr format '13:41:54'")
	arg = input()
	elimwhitespace = arg.replace(' ','')
	hour = elimwhitespace[:2]
	minute = elimwhitespace[3:5]
	sec = elimwhitespace[6:8]
	checker = elimwhitespace[8:]
	if hour.isdigit() and minute.isdigit() and sec.isdigit() and checker.isalpha() and len(elimwhitespace)==10:
		if int(minute)<60 and int(sec)<60:
			if checker.upper() == 'AM' and int(hour)<12:
				hr = str(int(hour)%12)
				n = "{}:{}:{}".format(hr,minute,sec)
				return n
			
			if checker.upper() == 'AM' and int(hour)==12:
				hr = "0" + str(int(hour)%12)
				n = "{}:{}:{}".format(hr,minute,sec)
				return n
			
			if checker.upper() == 'PM' and int(hour)<12:
				hr = str(int(hour)+12)
				n = "{}:{}:{}".format(hr,minute,sec)
				return n
			if checker.upper() == 'PM' and int(hour)==12:
				n = "{}:{}:{}".format(hour,minute,sec)
				return n
			if int(hour)>12:
				print("Hour should not be greater than 12 for this time format")
				return time()
			else:
				print("Time format should be either AM or PM")
				return time()
		else:
			print("minutes and seconds should be less than 60")
			return time()
		
	elif hour.isdigit() and minute.isdigit() and sec.isdigit() and len(elimwhitespace)==8:
		if int(minute)<60 and int(sec)<60:
			if (int(hour) > 0 and int(hour) < 12):
				n = "{}:{}:{}".format(hour,minute,sec)
				return n + ' AM'
			if int(hour) == 12:
				n = "{}:{}:{}".format(hour,minute,sec)
				return n + ' PM'
			if (int(hour) > 12 and int(hour) < 24):
				hr = str(int(hour)%12)
				n = "{}:{}:{}".format(hr,minute,sec)
				return n + ' PM'
			if int(hour)==0:
				hr = 12
				n = "{}:{}:{}".format(hr,minute,sec)
				return n + ' AM'
			else:
				print('Hour should be less than 24 for this time format')
				return time()
		else:
			print("minutes and seconds less than 60")
			return time()
	else:
		print("Hour, minute and second should contain only figures")
		return time()


def camelCase(name):
	var = name.replace('_',' ')
	print(var)
	c = var.split()
	print (c)
	c[1]=c[1].capitalize()
	print(c)
	d= "".join(c)
	print(d)
	return d

def console():
	print ('Enter the number sequence separated by commas')
	arg = input()
	



