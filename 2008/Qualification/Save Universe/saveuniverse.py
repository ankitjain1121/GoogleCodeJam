def saveuniverse():
	s = int(input())
	table = {}
	for i in range(s):
		table[input()]=i
	
	visited = [0]*s
	count = 0
	result = 0
	q = int(input())
	for i in range(q):
		query = input()
		if(visited[table[query]]!=1):
			if(count == (s-1)):
				result+=1
				count = 1
				visited = [0]*s
				visited[table[query]]=1
			else:
				visited[table[query]]=1
				count+=1
	return result	
def main():
	test_cases = int(input())
	for i in range(1,test_cases+1):
		print("Case #"+str(i)+": " + str(saveuniverse()))
	

if __name__ == "__main__":
	main()