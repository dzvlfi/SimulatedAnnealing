import random

def probs(awal,akhir,T):
	return 2.71828**(-(akhir-awal))/T

def simulated(x1,x2):
	return ((4-(2.1*(x1**2))+((x1**4)/3))*(x1**2))+(x1*x2)+((-4+(4*(x2**2)))*(x2**2))

x1,x2 = random.uniform(-10,10),random.uniform(-10,10)
awal = simulated(x1,x2)
T = 1000000
Tmin = 1
a = 0.9999

while (T>Tmin):
	y1,y2 = random.uniform(-10,10),random.uniform(-10,10)
	akhir = simulated(y1,y2)
	if (awal>akhir):
		awal = akhir
	elif (probs(awal,akhir,T)>random.random()):
		x1=y1
		x2=y2
	T *= a

print awal