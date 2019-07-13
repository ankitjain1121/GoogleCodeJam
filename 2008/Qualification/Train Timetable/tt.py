DEBUG = False		

def countTrains(depart,arival):
	d = len(depart)
	a = len(arival)
	i=0
	j=0
	count = 0
	balance = 0
	
	while(i < d and j < a):
		if DEBUG:
			print("d,a " + str(d) + "," + str(a) + " : " + str(i) + " , " + str(j))
		if(depart[i] < arival[j]):
			if(balance ==0 ):
				count += 1
			else:
				balance -= 1
			i += 1
		elif(depart[i] > arival[j]):
			balance += 1
			j += 1
		else:
			i += 1
			j += 1
	
	while(i < d):
		if(balance == 0):
			count += 1
		else:
			balance -= 1
		
		i += 1
			
	return count

def qsort(array,s,e):
	if(s >= e):
		return
		
	pivot = array[e]
	i = s
	j = e-1
	
	while(i <= j):
		if(array[i] > pivot):
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
			j -= 1
		else:
			i += 1
	
	temp = array[i]
	array[i] = pivot
	array[e] = temp
	qsort(array,s,i-1)
	qsort(array,i+1,e)
	
def sort(array):
	qsort(array,0,len(array)-1)

def processarray(array,wait):
	size = len(array)
	if DEBUG:
		print(size)
	for i in range(size):
		temp = array[i].split(":")
		temp[0] = int(temp[0])
		temp[1] = int(temp[1])
		
		temp[0] = temp[0] + int((temp[1] + wait)/60)
		temp[1] = (temp[1] + wait)%60
		
		array[i] = temp[0]*100 + temp[1]
	sort(array)

def solve(test_cases):
	for i in range(test_cases):
		wait = int(input())
		na,nb = input().split()
		na = int(na)
		nb = int(nb)
		
		a_arival = []
		a_depart = []
		b_arival = []
		b_depart = []
		
		if DEBUG:
			print(str(na) + " , " + str(nb))
		
		for temp in range(na):
			line  = input()
			a_depart.append(line.split()[0])
			b_arival.append(line.split()[1])
		for temp in range(nb):
			line = input()
			b_depart.append(line.split()[0])
			a_arival.append(line.split()[1])
			
			
		if DEBUG:
			print(a_arival)
			print(a_depart)
			print(b_arival)
			print(b_depart)

		processarray(a_arival,wait)
		processarray(a_depart,0)
		processarray(b_arival,wait)
		processarray(b_depart,0)
		
		if DEBUG:
			print(a_arival)
			print(a_depart)
			print(b_arival)
			print(b_depart)

		
		trainsa = (countTrains(a_depart,a_arival))
		trainsb = (countTrains(b_depart,b_arival))
		
		print("Case #" + str(i+1) + ": " + str(trainsa) + " " + str(trainsb))
		
def main():
	test_cases = int(input())
	solve(test_cases)

if __name__ == "__main__":
	main()