import time
now=time.localtime(time.time())
t1=time.strftime("%a %b %d-%m-%y",now)
t2=time.strftime("%H:%M:%S %p",now)
print(t1)
print(t2)
